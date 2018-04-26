/**
 * Created by yjw on 2018/3/19.
 */

!function(){
    var liData={
        name:"特朗普",
        keyWord:[
            {
                value: "140",
                key: "中共"
            },
            {
                value: "135",
                key: "中国"
            },
            {
                value: "134",
                key: "习近平"
            },
            {
                value: "126",
                key: "郭文贵"
            },
            {
                value: "121",
                key: "王岐山"
            }
        ]
    },
        keyWord =liData.keyWord;
        // keyWordLen =liData.keyWord;

    var ArrayLiPos =[];

    var keyPos =$('#relativity>span').position(),
        keyPosTop =keyPos.top,
        keyPosLeft =keyPos.left;


    for(var i=0,len=keyWord.length;i<len;i++){
        var key = keyWord[i].key,
            value = keyWord[i].value;
        // !function(index){
        //     htmlLi(key);
        //     liPosition(value,index)
        // }(i);
        htmlLi(key);
        liPosition(value,i)
    }

    //DOM
    function htmlLi(name){
        var html = "";
            html += '<li>';
            html+='   <div class="circle"></div>';
            html+='   <div class="cirName">'+name+'</div>';
            html+='</li>';

        $('#relativity>ul').append(html);
    }

    //算出位置,并存入ALiPos数组中,修改css
    function liPosition(pos ,i){

        var triHeight =Math.floor(pos*keyPosTop/(Math.sqrt(keyPosTop*keyPosTop+keyPosLeft*keyPosLeft))),
            triWidth =Math.floor(Math.sqrt(pos*pos-triHeight*triHeight));
        // console.log(triHeight);
        // console.log(triWidth);

        var liTop =Math.random()<=0.5?triHeight:triHeight+keyPosTop;
            liLeft =Math.random()<=0.5?triWidth:triWidth+keyPosLeft;
        //
        // // ALiPos[i].top =liTop;
        // // ALiPos[i].left =liLeft;
        //
        $('#relativity>ul li').eq(i).css({"top":liTop,"left":liLeft});

    }


}();