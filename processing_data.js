import {DOMParser} from "xmldom" 
import xpath from "xpath"



// 1. get document - Mongo



let doc = new DOMParser().parseFromString(page)

var xml = page;
// var doc = new DOMParser().parseFromString(xml);
const tab = doc.getElementById('tab')
const pattern = new RegExp("<th>(\w+)<[/]th>")
console.log(page.match(pattern))

//   var nodesTd = xpath.select("//td", tab);
//   var nodesTh = xpath.select("//td", tab);
// //   var nodesBody = xpath.select("/", doc);

//   nodes.forEach((e) => {
//     console.log(e.textContent)
  
    // console.log(Object.keys([index.toString()]))
  
  // newNodes.forEach(x => console.log(x))
  
// })
//   console.log(nodes.length)
//   nodesBody.forEach(e => console.log(e.textContent))
//   console.log(nodes[0].localName + ": " + nodes[0].firstChild.data);
//   console.log("Node: " + nodes[0].toString());
