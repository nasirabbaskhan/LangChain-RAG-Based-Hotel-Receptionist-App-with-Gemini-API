# LangChain RAG-Based Hotel Receptionist App

This project demonstrates the development of a **LangChain Retrieval-Augmented Generation (RAG) based Hotel Receptionist App**. The app utilizes **Google Gemini API** and **LangChain** to retrieve and generate responses to hotel-related queries using external knowledge in real-time. The app is designed to handle customer inquiries about hotel services, policies, room amenities, and local attractions, making it an intelligent assistant for hotel reception tasks.

## Features

- **Semantic Search with Google Gemini API**: Leverages Google's advanced Generative AI to understand queries and retrieve relevant information.
- **External Knowledge Retrieval**: Uses document embeddings and vector similarity search to retrieve precise hotel-related data (services, policies, etc.).
- **Real-time Response Generation**: Generates natural and accurate responses based on the retrieved content, enhancing customer interactions.
- **Document Chunking with LangChain**: Efficiently splits external knowledge documents for better search accuracy using LangChain's `CharacterTextSplitter`.
- **Embeddings with Google Generative AI**: Uses `GoogleGenerativeAIEmbeddings` to embed hotel information for accurate similarity search.

## Tech Stack

- **LangChain**: For text processing, embedding, and vector store creation.
- **Google Generative AI (Gemini API)**: For handling natural language processing, semantic search, and generation of responses.
- **Python**: Core language used for developing the app.
- **FAISS or LangChain's Vector Store**: For high-performance similarity search across embeddings.

## Prerequisites

1. **Python**: Make sure you have Python 3.7+ installed.
2. **Google API Key**: Required to access the Google Gemini API for LLM and embeddings.
3. **LangChain**: Install the LangChain package for document handling, chunking, and embedding generation.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/hotel-receptionist-app.git
    cd hotel-receptionist-app
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the environment variables:

    - Create a `.env` file in the root directory and add your Google API key:

    ```bash
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

1. **Run the app**:

    ```bash
    python app.py
    ```

2. The app will start asking for customer queries in a terminal interface:

    ```bash
    How can I help you?
    ```

3. Input any hotel-related query, and the app will retrieve relevant information based on the provided knowledge base.

## Sample Queries

- "What is the check-in time?"
- "Do you allow pets?"
- "What nearby attractions are available?"

## File Structure

- **`app.py`**: Main application script.
- **`data.txt`**: External knowledge file containing hotel-related information (services, policies, amenities).
- **`.env`**: Environment file containing the Google API key.
- **`requirements.txt`**: List of required packages for the project.

## External Knowledge Example

The knowledge base is stored in a text file (`data.txt`) containing information such as:

- **Hotel Services and Facilities**
- **Hotel Policies**
- **Local Attractions and Transportation**
- **Room Amenities**

## Future Improvements

- Implement a web interface for more user-friendly interaction.
- Integrate multi-language support for international guests.
- Add more advanced hotel-specific features such as booking management and customer feedback analysis.
