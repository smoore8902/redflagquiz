
function check_checkboxes() {
    var truth_list = []
    check_list = document.getElementsByTagName("input");
    for (let i =0; i <check_list.length; i++){
        //console.log(check_list)
        if (check_list[i].checked == true){
            truth_list.push(true);
        }
        else{
            truth_list.push(false)
        }
    }
    return truth_list
    
}