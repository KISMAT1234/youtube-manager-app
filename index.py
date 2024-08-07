import json
def load_data():
    try:
        with open('youtube.txt','r') as file:
            json.load(file)
    except FileNotFoundError:
        return []  
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. ")

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
