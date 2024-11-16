async function fetchAlbumArt(artistName, albumName) {
    const apiKey = 'de38ee5f15622aaec22b1468b97ca4ba'; // Replace with your actual Last.fm API key
    const response = await fetch(`http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=${apiKey}&artist=${encodeURIComponent(artistName)}&album=${encodeURIComponent(albumName)}&format=json`);
    
    const data = await response.json();
    
    if (data.album && data.album.image) {
      // The last item in the image array is usually the largest size
      const imageUrl = data.album.image[data.album.image.length - 1]['#text'];
      return imageUrl; // This is the URL for the album cover image
    } else {
      console.log('Album art not found.');
      return null;
    }
  }

  async function displayAlbumArt(artistName, albumName) {
    const albumArtUrl = await fetchAlbumArt(artistName, albumName);
    if (albumArtUrl) {
      document.getElementById("album-art").src = albumArtUrl;
    }
  }
  
  // Example usage
  displayAlbumArt("AP Dhillon", "Brownprint"); // Replace with desired artist and album name