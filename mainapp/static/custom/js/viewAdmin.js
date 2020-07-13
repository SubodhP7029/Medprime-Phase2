var selectedRowData

//   $('#adminTable tbody').on('click', 'tr', function () {
//     selectedRowData = table.row(this).data();
//     alert(selectedRowData)
// });

// var table = $('#adminTable').DataTable({
// });

$(document).ready(function () {
$('#adminTable tbody').on('click', 'tr', function () {
    var tableData = $(this).children("td").map(function () {
        return $(this).text();
    }).get();
  
    // var a = document.createElement('a')
    // link = "/editAdmin"
    // a.href = link + '/' + tableData[0]
    // document.getElementById('editbutton').innerHTML = ''
    // document.getElementById('editbutton').appendChild(a)
    alert("Your data is: " + $.trim(tableData[0]) + " , " + $.trim(tableData[1]) + " , " + $.trim(tableData[2])+ " , " + $.trim(tableData[3])+ " , " + $.trim(tableData[4]));

});

});
    

function removeAdmin(selectedRowData) {

    var id = document.getElementById('adminid').value
    //var loggedinuser = document.getElementById('currentloggedinuser').value
    var delteQuery = 'DELETE FROM mainapp_adminprofile WHERE id = ' + id
    $.get("/removeadmin", { sqlParam: delteQuery }, function (data) {
        console.log(data)
        $('#deleteAdmin').modal('hide');
    })
}


// $('#invoiceTables tbody').on('click', 'tr', function () {
//     selectedRowData = table.row(this).data();
//     var a = document.createElement('a')
//     link = "/cloninginvoice"
//     a.href = link + '/' + selectedRowData[0]
//     a.innerText = 'Clone'
//     document.getElementById('cloningid').innerHTML = ''
//     document.getElementById('cloningid').appendChild(a)
//     var a = document.createElement('a')
//     link = "/editinginvoice"
//     a.href = link + '/' + selectedRowData[0]
//     a.innerText = 'Edit'
//     document.getElementById('editid').innerHTML = ''
//     document.getElementById('editid').appendChild(a)
//     $('#optionsModal').modal('show');
// });