
### 執行：
ansible-playbook build_node.yml -K

### 心得：
最近找工作看到有些職缺有Ansible經驗需求，好奇這東西這的有這麼好用大家都愛用嗎，所以又來玩了一下Ansible。
* 這次多加了從建立Python環境和Git拉code的功能，使得整個自動化變得更完整，也讓playbook腳本變得更冗長
* 試用了 Role 的用法，希望可以讓這些playbook更靈活運用，也可以reuse
  覺得還不錯的教學：
  https://www.digitalocean.com/community/tutorials/how-to-use-ansible-roles-to-abstract-your-infrastructure-environment
* 原來 hosts 也可以用yml格式
* 還是覺得ansible很不易上手，沒辦法自己猜出playbook寫法，做什麼都需要查Google看文件，研究module的參數。就算要用平常常用的工具，也像是學一套新工具。
* 踩到的雷：
  * super user權限：
    Docker操作需要加上become提升權限執行，但如果全操作都用super user權限，感覺太危險。
    最後只好必須把docker和其他操作分開在不同的play裡，一個有become，另一個不用。

  * 使用virtualenv的Python：
    使用docker module需要在managed node上裝好Python的docker套件
    為了保持node主機環境乾淨，我使用virtualenv來建立自己Ansible需要的Python環境
    造成我的playbook中，前後需要使用不同的 ansible_python_interpreter
    想到的方法只有在role的vars裡指定，不role自己目前要用的Python環境
    這樣做不好的地方是不同role之間存在implicit相依性，例如 docker role 必須在 git role之後，否則找不到Python docker package
    不知道該怎麼解，仍然Ansible苦手
    
回到一開始在想Ansible有什麼好處，讓很多人選擇使用它。
往Ansible和Shell Script的差別來思考，雖然Ansible要做的事Shell Script透過良好的架構設計也能達成，
但Ansible像是公訂了一套規格，讓多hosts和多腳本有一定的格式，讓不同開發者能省去一些溝通成本和分享共用role或playbook。
加上考慮Ansible編寫較高成本，覺得應該要依使用情境來選擇工具，在少量簡單的自動化還是可以用Shell Script，
大量複雜操作，需要多人協作，或是有不熟悉工具的現成腳本可使用時，則可以使用Ansible。

