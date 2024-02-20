# Server YouTube Uploader

This project is designed to automatically upload videos to a YouTube channel from a specified directory. It's ideal for creators looking for an automated solution to manage video uploads. The uploader monitors a folder for new videos and uploads them to YouTube as private videos, using Docker containers for a seamless, scalable solution.

## Features

- **Automatic Video Uploads**: Automatically detects and uploads videos to a specified YouTube channel.
- **Dockerized**: Runs in a Docker container for easy deployment and scalability.
- **Privacy Focused**: Uploads videos as private, allowing you to review them before making them public.
- **Flexible**: Watch any directory for new video files, easily configurable to suit your needs.

## Getting Started

### Prerequisites

- Docker
- Python 3.9 or later
- Google API credentials for YouTube Data API v3

### Installation

1. Clone this repository to your local machine or server where Docker is installed:

   ```bash
   git clone https://github.com/jay0718/jay0718-server_youtube_uploader.git
   ```

2. Navigate into the project directory:

```bash
cd jay0718-server_youtube_uploader
```

3. Build the Docker container:

```bash
docker build -t youtube-uploader .
```

4. Run the Docker container, replacing `/mnt/youtube_uploader/video` with the path to the directory you want to monitor for new video uploads:
```bash
docker run -d --name youtube-uploader-instance -v /path/to/your/videos:/app/videos youtube-uploader
```

### Configuration

1. Obtain Google API credentials and save them as `client_secrets.json` in the project directory.
2. Configure the `video_uploader.py` script with your desired YouTube channel and privacy settings.

## Usage

Place video files into the monitored directory. The uploader will automatically detect and upload new videos to your YouTube channel as private videos.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or add new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
