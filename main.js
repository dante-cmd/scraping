import { By, Key, Builder, until } from "selenium-webdriver";
// import  {chrome} from 'selenium-webdriver/chrome';
import chromedriver from "chromedriver"
import Pages from "./models/Pages.js";
import connectDB from "./lib/dbConnect.js";


// // This has the 

// const createDriver = async () =>{
//   let driver = await new Builder()
//   .forBrowser("chrome")
//   .setChromeOptions(new chrome.Options().headless())
//   .build();
//   // await driver.get(url)
//   return driver
// }

// const switchDriver = async (driver) => {
//   const alertTo = await driver.switchTo().alert();

//   await alertTo.sendKeys("Dante");
//   await alertTo.accept();
  
//   return driver
// }


async function test_case() {
  await connectDB();

  let driver = await new Builder().forBrowser("chrome").build();
  // .setChromeOptions(new chrome.Options().headless())
  

  const url = "http://127.0.0.1:5502/scraping/api/index.html"

  await driver.get(url);

  // await driver.wait(() => until.elementLocated(By.css('tbody')), 10000)
  
  
  // const alertTo = await driver.switchTo().alert();
  // // const alertas = await driver.switchTo().alert().getText()

  // // console.log(alertas)
  // await alertTo.sendKeys("Dante");

  // await alertTo.accept();

  const page = await driver.getPageSource();

  await Pages.collection.insertOne({body:page})
  // const result = await Pages.aggregate(query);

 
  
  setInterval(function () {
    driver.quit(), 200000;
  });
}
// test_case()

setTimeout(() => {
  test_case();
}, 40000)
// setTimeout(() => {
//   test_case();
// }, 40000)

