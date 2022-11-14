import mongoose from "mongoose";

const PagesSchema = new mongoose.Schema(
  {
    body:String
  },
  { collection: "Pages" }
);
const Pages = mongoose.models.Pages || mongoose.model("Pages", PagesSchema);

export default Pages;
