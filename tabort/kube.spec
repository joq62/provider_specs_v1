{provider_spec,"kube",
 [
     {appl_name,"kube"},
     {vsn,"0.1.0"},
     {app_name,"kube"},
     {app,kube},
     {dir,"kube"},
     {tar_file,"kube-0.1.0.tar.gz"},
     {node_name,"kube"},
     {cookie,"a_cookie"},
     {pa_args," -pa kube/lib/*/ebin -config kube/config/sys.config "},
     {git_path,"https://github.com/joq62/kube.git"},
     {tar_cmd,"tar -xvf kube/kube-0.1.0.tar.gz -C kube "},
     {start_cmd,{application,start,[kube],20000}},
     {num, 1},
     {affinity,[all_hosts]}
 ]
}.
