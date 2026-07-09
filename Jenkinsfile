pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code downloaded from GitHub'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t book-manager-pipeline:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                    docker stop book-manager-pipeline-container || true
                    docker rm book-manager-pipeline-container || true
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                    docker run -d \
                   --name book-manager-pipeline-container \
                 -p 5002:5000 \
                 -v book-manager-data:/app/data \
                 -e DATABASE_PATH=/app/data/books.db \
                 book-manager-pipeline:latest
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    sleep 3
                    docker ps
                    curl --fail http://localhost:5002
                '''
            }
        }
    }

    post {
        success {
            echo 'Book Manager deployment completed successfully!'
        }

        failure {
            echo 'Book Manager deployment failed!'
        }
    }
}