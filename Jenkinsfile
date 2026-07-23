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
                sh '''
                    python3 -m pip install --user -r requirements.txt
                    python3 -m unittest test_app.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t book-manager-pipeline:latest .
                '''
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
                      --add-host=host.docker.internal:host-gateway \
                      -e DB_HOST=host.docker.internal \
                      -e DB_PORT=3306 \
                      -e DB_NAME=book_manager \
                      -e DB_USER=bookuser \
                      -e DB_PASSWORD=bookpass \
                      book-manager-pipeline:latest
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    sleep 5
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
            sh 'docker logs book-manager-pipeline-container || true'
            echo 'Book Manager deployment failed!'
        }
    }
}