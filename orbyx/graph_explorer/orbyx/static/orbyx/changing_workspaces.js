
function open_workspace(event, workspace_name){
    var tabs = document.getElementsByClassName("tab")
    for(i = 0; i < tabs.length; i++) {
        tabs[i].classList.remove("tab-selected");
    }
    var selectedTab = document.getElementById(workspace_name);
    selectedTab.classList.add("tab-selected");
}