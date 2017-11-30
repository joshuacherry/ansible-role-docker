FROM centos

ENV TERM=xterm

# Install systemd -- See https://hub.docker.com/_/centos/
RUN yum -y update; yum clean all; \
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

RUN yum install -y --enablerepo=extras epel-release wget sudo \ 
    && wget -O /tmp/ansible.rpm https://releases.ansible.com/ansible/rpm/release/epel-7-x86_64/ansible-2.4.2.0-1.el7.ans.noarch.rpm \
    && yum install -y /tmp/ansible.rpm \
    && rm /tmp/ansible.rpm \
    && yum clean all

# Disable requiretty.
RUN sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/'  /etc/sudoers

    # Get version pip available versions
    # pip3 install ansible==randomwords

COPY chef.asc /tmp/chef.asc
COPY chef-stable.list /etc/yum.repos.d/chef-stable.repo

RUN rpm --import /tmp/chef.asc \
    && yum install -y inspec-1.43.5-1.el7

VOLUME ["/sys/fs/cgroup"]
CMD ["/usr/sbin/init"]