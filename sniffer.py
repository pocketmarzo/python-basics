import sys
from PIL import Image
from PIL.ExifTags import TAGS
from pillow_heif import register_heif_opener


register_heif_opener()

def get_decimal_from_dms(dms, ref):
    
    degrees = float(dms[0])
    minutes = float(dms[1]) / 60.0
    seconds = float(dms[2]) / 3600.0
    coordinate = degrees + minutes + seconds
    if ref in ['S', 'W']:
        coordinate = -coordinate
    return coordinate

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python sniffer.py image.jpg")

    img_path = sys.argv[1]

    try:
        img = Image.open(img_path)
        exif_data = img.getexif()

        if not exif_data:
            sys.exit(f"\n[!] No metadata found in '{img_path}'. Data might be stripped.")

        
        print(f"\n{'PARAMETER':<25} | {'VALUE'}")
        print("-" * 65)

        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            
            
            val_display = f"<{len(value)} bytes>" if isinstance(value, bytes) else value
            print(f"{str(tag_name):<25} | {val_display}")

        # --- GPS EXTRACTION ---
        # 0x8825 is the tag ID for GPS Info IFD
        gps_info = exif_data.get_ifd(0x8825)

        if gps_info:
            try:
                
                lat_ref = gps_info[1]
                lat_dms = gps_info[2]
                lon_ref = gps_info[3]
                lon_dms = gps_info[4]

                latitude = get_decimal_from_dms(lat_dms, lat_ref)
                longitude = get_decimal_from_dms(lon_dms, lon_ref)

                print(f"\n" + "="*65)
                print(f"LOCATION FOUND")
                print(f"Coordinates: {latitude}, {longitude}")
                print(f"Google Maps: https://www.google.com/maps?q={latitude},{longitude}")
                print("="*65)
            except (KeyError, IndexError):
                print("\n[!] GPS tags found, but data is corrupted or incomplete.")
        else:
            print("\n[!] GPSInfo block is empty. Geotagging was likely disabled.")

    except FileNotFoundError:
        sys.exit(f"Error: File '{img_path}' not found.")
    except Exception as e:
        sys.exit(f"Analysis error: {e}")

if __name__ == "__main__":
    main()