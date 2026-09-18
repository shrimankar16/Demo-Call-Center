# AI-Powered Call Center Analytics Platform

> 🎯 An advanced analytics platform leveraging Large Language Models (LLMs) and MLRun to transform call center audio data into actionable insights through automated transcription, sentiment analysis, and intelligent feature extraction.

![Call Center Analytics](./images/call-center-readme.png)

## 🚀 Overview

This platform demonstrates the power of modern AI/ML workflows for call center operations. It showcases:

- **Automated Data Generation**: Synthetic call data creation with realistic conversations
- **Audio Processing**: Speech diarization and multi-speaker detection
- **AI-Powered Transcription**: Convert audio to text using state-of-the-art models
- **Privacy Protection**: Automatic PII detection and redaction using Microsoft Presidio
- **Intelligent Analysis**: Extract insights, sentiment, and key metrics using LLMs
- **Interactive Visualization**: Real-time dashboard with Vizro for data exploration

## ✨ Key Features

### 🎤 Speech Processing
- **Speech Diarization** with Silero VAD
- **Multi-language Transcription** using OpenAI Whisper
- **Audio Synthesis** for test data generation
- **Batch Processing** for high-volume scenarios

### 🧠 AI-Powered Analytics
- **Sentiment Analysis** to gauge customer satisfaction
- **Topic Extraction** to identify common issues
- **Call Summarization** for quick insights
- **Agent Performance** metrics and scoring
- **Automated Tagging** and categorization

### 🔒 Privacy & Compliance
- **PII Detection** using Flair NLP and Presidio
- **Data Anonymization** to protect sensitive information
- **Secure Storage** with encrypted databases
- **Audit Trails** for compliance reporting

### 📊 Visualization & Reporting
- **Interactive Dashboards** built with Vizro
- **Real-time Metrics** tracking
- **Call Playback** with synchronized transcripts
- **Export Capabilities** for reporting

## 🏗️ Architecture

![Workflow Architecture](./images/call-center-workflow.png)

The platform uses **MLRun** for orchestration, providing:
- ⚡ Auto-scaling based on workload
- 📝 Automatic logging and versioning
- 🔄 Seamless data passing between pipeline steps
- 🎯 Resource optimization (CPU/GPU)

## 📋 Prerequisites

- **Python** 3.9, 3.10, or 3.11
- **MLRun** 1.9+ (automatically installed)
- **OpenAI API Key** for conversation generation and analysis
- **SQLite** or **MySQL** for data storage
- **Optional**: NVIDIA GPU for faster processing

### Technology Stack

| Component | Technology |
|-----------|-----------|
| ML Framework | MLRun, HuggingFace Transformers |
| Speech Processing | OpenAI Whisper, Silero VAD |
| NLP & PII | Flair, Microsoft Presidio |
| LLM | OpenAI GPT-4 |
| Visualization | Vizro (Plotly + Dash) |
| Database | SQLite / MySQL |
| Orchestration | MLRun Pipelines |

## ⚙️ Installation

### Quick Start (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/shrimankar16/Demo-Call-Center.git
   cd Demo-Call-Center
   ```

2. **Create virtual environment** (Python 3.11 recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt -r dev-requirements.txt
   ```

4. **Configure API keys**
   ```bash
   cp env.template .env
   # Edit .env and add your OPENAI_API_KEY and OPENAI_API_BASE
   ```

5. **Launch Jupyter Lab**
   ```bash
   jupyter lab
   ```

### Using Conda

```bash
conda create -n call-center python=3.11 ipykernel graphviz pip
conda activate call-center
pip install -r requirements.txt
```

### Using Docker

```bash
make mlrun-docker
# MLRun UI will be available at http://localhost:8060
```

## 🎯 Usage

### 1. Generate Synthetic Call Data

Open `notebook_1_generation.ipynb` and follow these steps:

- **Create Project**: Initialize MLRun project with all configurations
- **Generate Agents & Clients**: Create realistic profiles
- **Create Conversations**: Use LLM to generate realistic dialogues
- **Synthesize Audio**: Convert text conversations to audio files
- **Create Batches**: Prepare data for analysis pipeline

💡 **Tip**: You can skip generation and use pre-generated data from `example_data/`

### 2. Analyze Call Data

Open `notebook_2_analysis.ipynb` to process calls:

- **Load Call Data**: Import audio files into the system
- **Diarization**: Detect speaker changes
- **Transcription**: Convert speech to text
- **PII Recognition**: Identify and redact sensitive information
- **LLM Analysis**: Extract insights, sentiment, and summaries
- **Visualization**: View results in interactive dashboard

### 3. View Results

**Option A: Vizro Dashboard** (Interactive)
```python
# Run from notebook_2_analysis.ipynb
project.deploy_function("call-center-ui")
```
Access at: `http://localhost:8050`

**Option B: MLRun UI** (Pipeline Monitoring)
Access at: `http://localhost:8060` (if using Docker)

![Dashboard Screenshot](./images/call-center-ui.png)

## 📁 Project Structure

```
Demo-Call-Center/
├── src/                          # Source code
│   ├── calls_generation/         # Data generation modules
│   │   ├── conversations_generator.py
│   │   └── skip.py
│   ├── calls_analysis/           # Analysis modules  
│   │   ├── db_management.py
│   │   └── postprocessing.py
│   ├── workflows/                # MLRun workflows
│   │   ├── calls_generation.py
│   │   └── calls_analysis.py
│   └── common.py                 # Shared utilities
├── vizro/                        # Dashboard application
│   ├── app.py                    # Main Vizro app
│   ├── custom_charts.py          # Custom visualizations
│   └── custom_components.py      # UI components
├── data/                         # Generated data storage
├── example_data/                 # Sample datasets
├── notebook_1_generation.ipynb   # Data generation notebook
├── notebook_2_analysis.ipynb     # Analysis notebook
├── project_setup.py              # MLRun project configuration
└── requirements.txt              # Python dependencies
```

## 🔧 Configuration

### Environment Variables

Edit `.env` file:

```env
OPENAI_API_KEY=your-openai-api-key-here
OPENAI_API_BASE=https://api.openai.com/v1
MYSQL_URL=mysql+pymysql://user:pass@host/db  # Optional
```

### Project Parameters

Key settings in `project_setup.py`:

```python
use_sqlite = True          # Use SQLite instead of MySQL
gpus = 0                   # Number of GPUs (0 for CPU-only)
build_image = False        # Build custom Docker image
skip_calls_generation = False  # Use existing data
```

## 🎓 Learning Resources

### Understanding the Workflow

1. **Data Generation Pipeline**
   - Synthetic data creation with realistic scenarios
   - Leverages GPT for natural conversation generation
   - Audio synthesis with multiple voice profiles

2. **Analysis Pipeline**
   - Speaker diarization to separate speakers
   - Whisper-based transcription
   - PII detection with Presidio
   - LLM-based feature extraction

3. **MLRun Integration**
   - Function-based architecture
   - Automatic artifact management
   - Pipeline orchestration
   - Resource optimization

### Key Concepts

- **MLRun Functions**: Reusable, scalable ML functions from the [MLRun Hub](https://www.mlrun.org/hub/)
- **Workflows**: DAG-based pipelines connecting multiple functions
- **Artifacts**: Versioned outputs (models, data, logs)
- **Serving**: Deploy models/apps as microservices

## 🚨 Important Notes

⚠️ **Processing Time**: Full pipeline can take 1-2 hours without GPU acceleration

⚠️ **API Costs**: OpenAI API usage will incur charges based on your usage

⚠️ **Data Privacy**: Ensure compliance with local data protection regulations when processing real call data

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

```
Copyright 2024 Shrijay Mankar

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
```

## 🙏 Acknowledgments

- **MLRun** for the orchestration framework
- **OpenAI** for GPT and Whisper models
- **Microsoft** for Presidio PII detection
- **Vizro** for the visualization framework
- **HuggingFace** for the transformers library

## 📧 Contact

**Shrijay Mankar**
- GitHub: [@shrimankar16](https://github.com/shrimankar16)
- Project Link: [https://github.com/shrimankar16/Demo-Call-Center](https://github.com/shrimankar16/Demo-Call-Center)

---

⭐ If you find this project useful, please consider giving it a star!

**Built with ❤️ by Shrijay Mankar**
