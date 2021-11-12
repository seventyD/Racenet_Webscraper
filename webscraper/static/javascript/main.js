function get_text()
{
    var txtFile = new XMLHttpRequest();
    txtFile.open("GET", "out.txt", true);
    txtFile.onreadystatechange = function() {
      if (txtFile.readyState === 4 && txtFile.status == 200) {
         allText = txtFile.responseText;
      }
    document.getElementById('winners').innerHTML = allText;
}
}