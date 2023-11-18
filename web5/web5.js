// Import the Web5 library
import { Web5 } from 'https://cdn.jsdelivr.net/npm/@tbd54566975/web5@0.7.9/dist/browser.mjs';

/**
 * Function to create a new Decentralized Identifier (DID) and a Decentralized Web Node (DWN).
 * It also communicates data between nodes using Web5.
 */
async function initializeGame(gameData) {
  try {
    // Connect to Web5 and create a new DID
    const { web5, did: myDid } = await Web5.connect();

    // Log the created/connected DID
    console.log('Initialized Game with DID:', myDid);

    // Communicate game data between nodes
    const { record, status } = await web5.dwn.records.write({
      data: gameData,
      message: {
        protocol: 'https://example.com/game/protocol',
        protocolPath: 'path/to/game/data',
        schema: 'gameData',
        recipient: 'did:ion:EiD3a17O2DCebpcZli-1BHRtMQ0LtTfrU85hHnAux6LrRQ'
      }
    });

    // Handle the response and check the status code
    if (status === 200) {
      console.log('Game data successfully updated:', record);
    } else {
      console.error('Failed to update game data. Status:', status);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

// Call the function to initialize the game
initializeGame();
