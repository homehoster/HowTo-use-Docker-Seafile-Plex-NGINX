#!/bin/bash

#mit diesem Script wird erreicht, dass nach einer SystemNeuinstallation
#grundlegende Einstellungen vorgenommen werden

#Programme installieren
apt-get update -y && apt-get dist-upgrade -y
apt-get -y install davfs2

#Docker mit apt intallieren
docker network create extern
