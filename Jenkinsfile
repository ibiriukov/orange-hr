pipeline {
  agent any

  parameters {
    booleanParam(name: 'HEADED', defaultValue: false, description: 'Run browser in headed mode')
  }

  stages {
    stage('Checkout'){ steps { checkout scm } }

    stage('Setup'){
      steps {
        bat '''
          echo ==== Create venv and install pip ====
          py -3 -m venv .venv
          call .venv\\Scripts\\activate
          pip install --upgrade pip wheel

          echo ==== Install requirements ====
          pip install -r requirements.txt

          echo ==== Install Playwright browsers ====
          py -3 -m playwright install
        '''
      }
    }

    stage('Test'){
      steps {
        withCredentials([
          usernamePassword(credentialsId: 'orangehrm-creds',
                           usernameVariable: 'ORANGE_USERNAME',
                           passwordVariable: 'ORANGE_PASSWORD'),
          string(credentialsId: 'orangehrm-base-url',
                 variable: 'ORANGE_BASE_URL')
        ]) {
          bat """
            call .venv\\Scripts\\activate
            set HEADED=%HEADED%
            echo HEADED=%HEADED%
            pytest -v --junitxml=test-results\\junit.xml ^
                   --html=report.html --self-contained-html
          """
        }
      }
    }
  }

  post {
    always {
      // Make sure a junit file exists so publishing never breaks the build display
      bat 'if not exist test-results mkdir test-results & if not exist test-results\\junit.xml type NUL > test-results\\junit.xml'
      junit 'test-results/junit.xml'
      archiveArtifacts artifacts: 'report.html,test-results/**', fingerprint: true, onlyIfSuccessful: false
    }
  }
}
