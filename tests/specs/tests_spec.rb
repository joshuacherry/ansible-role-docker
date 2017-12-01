# encoding: utf-8

control '01' do
  impact 0.7
  title 'Verify docker-ce service'
  desc 'Ensures docker-ce service is up and running'
  
  describe package('docker-ce') do
    it { should be_installed }
  end

  describe service('docker') do
    it { should be_running }
    it { should be_enabled }
  end

  describe pip('docker-compose') do
    it { should be_installed }
  end

  describe user('testuser') do
    its('groups') { should eq ['testuser', 'docker']}
  end
end
