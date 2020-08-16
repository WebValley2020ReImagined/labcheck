# Environment set up for WebValley2020 on Azure Lab

## Are you a Windows user?
### Open Windows PowerShell with Administratory Rights

`Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0`

## Open a terminal and
## connect to the virtual machine (VM)
`ssh -L 8888:localhost:8888 -p 63686 gabriele@ml-lab-0ef8dec9-10b7-43cb-910d-e1ff4cd78d15.westeurope.cloudapp.azure.com`

## Activate the conda environment called py37_pytorch
`conda activate py37_pytorch`

## Start jupyter lab
`jupyter lab --no-browser`

## Navigate to http://localhost:8888/lab
