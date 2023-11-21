pipeline {
    agent any
    
    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('0cbe62e8-4221-48f0-9f2b-cb9a03a0d9dc')
	CI = 'true'
    }		

    stages {
	stage('Deploy to GCP') {
            steps {
                sh 'gcloud auth activate-service-account --key-file ${env.GOOGLE_APPLICATION_CREDENTIALS}'
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
