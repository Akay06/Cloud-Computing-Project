pipeline {
    agent any
    
    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('ultra-thought-397322')
	CI = 'true'
    }		

    stages {
	stage('Deploy to GCP') {
            steps {
                sh 'gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS'
                sh 'gcloud compute instances list'
            }
        }
        stage('Build') {
            steps {
                sh 'pip install flask'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python -m flask run'
            }
        }
    }
}
