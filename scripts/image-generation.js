const { createCanvas, loadImage, registerFont } = require("canvas");
const fs = require("fs");
registerFont("./static/fonts/PressStart2P-Regular.tff", {
  family: "Press Start 2P",
});

registerFont("./static/fonts/NotoSans-Bold.ttf", {
  family: "Noto Sans",
});

let c = {
  width: 1200,
  height: 700,
};

const canvas = createCanvas(c.width, c.height);
const ctx = canvas.getContext("2d");

exports.generateTeraSaturdayImage = (blogName, postNumber, defaultImage) => {
  const canvas = createCanvas(c.width, c.height);
  const ctx = canvas.getContext("2d");
  ctx.save();
  loadImage(defaultImage).then((image) => {
    
    ctx.drawImage(image, 0, 0, c.width, c.height);

    let postid = postNumber;

    ctx.font = '100px "Press Start 2P"';

    ctx.strokeStyle = "black";
    ctx.lineWidth = 18;
    ctx.lineCap = "round";
    ctx.strokeText("Tera", c.width / 2 - c.height / 2 - 150, c.height / 3);
    ctx.fillStyle = "white";
    ctx.fillText("Tera", c.width / 2 - c.height / 2 - 150, c.height / 3);

    spacer = ctx.measureText("Tera").width;
    ctx.globalAlpha = 0.5;
    ctx.font = '100px "Press Start 2P"';
    ctx.strokeStyle = "black";
    ctx.lineWidth = 18;
    ctx.lineCap = "round";
    ctx.strokeText("sology", c.width / 2 - 90, c.height / 3);

    ctx.fillStyle = "white";
    ctx.fillText("sology", c.width / 2 - 90, c.height / 3);
    ctx.fillStyle = "white";
    ctx.fillText("sology", c.width / 2 - 90, c.height / 3);
    ctx.fillStyle = "white";
    ctx.fillText("sology", c.width / 2 - 90, c.height / 3);
    ctx.fillStyle = "white";
    ctx.fillText("sology", c.width / 2 - 90, c.height / 3);

    ctx.globalAlpha = 1;
    ctx.translate(-100, 150);
    ctx.rotate(10 * (-Math.PI / 180));
    ctx.font = 'bold 130px "Noto Sans"';
    ctx.strokeStyle = "black";
    ctx.lineWidth = 25;
    ctx.strokeText("Saturday", c.width / 2 - 20, c.height / 3);
    ctx.fillStyle = "#E8BE36";
    ctx.fillText("Saturday", c.width / 2 - 20, c.height / 3);

    var pst =
      ctx.measureText("sology").width - ctx.measureText(postid).width + 70;

    ctx.restore();

    ctx.font = 'bold 100px "Noto Sans"';
    ctx.strokeStyle = "black";
    ctx.lineWidth = 25;
    ctx.strokeText(postid, pst + c.width / 2 + 60, c.height / 3 + 120);
    ctx.fillStyle = "#E8BE36";
    ctx.fillText(postid, pst + c.width / 2 + 60, c.height / 3 + 120);
    ctx.restore();

    let buffer = canvas.toBuffer("image/png");
    fs.writeFileSync("./blog/" + blogName + "/cover.jpg", buffer);
  });
};
