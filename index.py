def list_all_video(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos = []
    while True:
        print("5. Youtube manager")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Exit the app")
        choice = input("Enter your choice")
    
        match choice:
            case'1':
                list_all_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
        
if __name__ == "__main__":
    main()
