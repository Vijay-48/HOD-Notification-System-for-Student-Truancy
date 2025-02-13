# main.py

from inference.live_detection import process_cctv_stream

def main():
    print("Starting HOD Notification System for Student Truancy...")
    process_cctv_stream()

if __name__ == "__main__":
    main()
