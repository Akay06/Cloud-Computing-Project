pipeline {
    agent any
    
    stages {		
		
		stage('build') {
			steps {
				withCredentials([file(credentialsId: 'gcloud', variable: 'GCLOUD_CREDS')]){
					sh '''
						gcloud compute instances create in-class-lab3-application --project=ultra-thought-397322 --zone=us-central1-a --machine-type=e2-medium --network-interface=network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=default --metadata=startup-script="sudo apt-get -y update && sudo apt-get install -y python3-pip && pip3 install flask" --maintenance-policy=MIGRATE --provisioning-model=STANDARD --service-account=1018379038222-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=http-server --create-disk=auto-delete=yes,boot=yes,device-name=in-class-lab3-application,image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20231101,mode=rw,size=10,type=projects/ultra-thought-397322/zones/us-central1-a/diskTypes/pd-balanced --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --labels=goog-ec-src=vm_add-gcloud --reservation-affinity=any || true
						'''
				}
				sleep(time:120,unit:"SECONDS") 
			}
		}
		
		stage('test') {
			steps {
				withCredentials([file(credentialsId: 'gcloud', variable: 'GCLOUD_CREDS')]){
					sh '''
						gcloud compute ssh --zone "us-central1-a" "in-class-lab3-application" --project "ultra-thought-397322" --command "python3 --version"
					'''
				}
			}
		}
		
		stage('deploy') {
			steps {
				withCredentials([file(credentialsId: 'gcloud', variable: 'GCLOUD_CREDS')]){
					sh '''
						gcloud compute ssh --zone "us-central1-a" "in-class-lab3-application" --project "ultra-thought-397322" --command "git clone https://github.com/Akay06/Cloud-Computing-Project/ && cd Cloud-Computing-Project/ && nohup python3 app.py </dev/null >nohup.out 2>nohup.err &"
					'''
				}
			}
		}
    }
}
