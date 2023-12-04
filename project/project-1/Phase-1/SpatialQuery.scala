package cse511

import org.apache.spark.sql.SparkSession
import scala.math._

object SpatialQuery extends App{
    
    
    
  def runRangeQuery(spark: SparkSession, arg1: String, arg2: String): Long = {

    val pointDf = spark.read.format("com.databricks.spark.csv").option("delimiter","\t").option("header","false").load(arg1);
    pointDf.createOrReplaceTempView("point")

    // YOU NEED TO FILL IN THIS USER DEFINED FUNCTION


    spark.udf.register("ST_Contains",(queryRectangle:String, pointString:String)=>{
        val points = pointString.split(",").map(_.toDouble)
        val point_x = points(0)
        val point_y = points(1)
        val rectangle = queryRectangle.split(",").map(_.toDouble)
        val rect_xmin = rectangle(0)
        val rect_ymin = rectangle(1)
        val rect_xmax = rectangle(2)
        val rect_ymax = rectangle(3)
        point_x >= rect_xmin && point_x <= rect_xmax && point_y >= rect_ymin && point_y <= rect_ymax
    })

    val resultDf = spark.sql("select * from point where ST_Contains('"+arg2+"',point._c0)")
    resultDf.show()

    return resultDf.count()
  }

  def runRangeJoinQuery(spark: SparkSession, arg1: String, arg2: String): Long = {

    val pointDf = spark.read.format("com.databricks.spark.csv").option("delimiter","\t").option("header","false").load(arg1);
    pointDf.createOrReplaceTempView("point")

    val rectangleDf = spark.read.format("com.databricks.spark.csv").option("delimiter","\t").option("header","false").load(arg2);
    rectangleDf.createOrReplaceTempView("rectangle")

    // YOU NEED TO FILL IN THIS USER DEFINED FUNCTION
    spark.udf.register("ST_Contains",(queryRectangle:String, pointString:String)=>{
        val points = pointString.split(",").map(_.toDouble)
        val point_x = points(0)
        val point_y = points(1)
        val rectangle = queryRectangle.split(",").map(_.toDouble)
        val rect_xmin = rectangle(0)
        val rect_ymin = rectangle(1)
        val rect_xmax = rectangle(2)
        val rect_ymax = rectangle(3)
        point_x >= rect_xmin && point_x <= rect_xmax && point_y >= rect_ymin && point_y <= rect_ymax
    })

    val resultDf = spark.sql("select * from rectangle,point where ST_Contains(rectangle._c0,point._c0)")
    resultDf.show()

    return resultDf.count()
  }

  def runDistanceQuery(spark: SparkSession, arg1: String, arg2: String, arg3: String): Long = {

    val pointDf = spark.read.format("com.databricks.spark.csv").option("delimiter","\t").option("header","false").load(arg1);
    pointDf.createOrReplaceTempView("point")

    // YOU NEED TO FILL IN THIS USER DEFINED FUNCTION
    spark.udf.register("ST_Within",(pointString1:String, pointString2:String, distance:Double)=>{
        val point1 = pointString1.split(",").map(_.toDouble) 
        val x1 = point1(0)
        val y1 = point1(1)
        val point2 = pointString2.split(",").map(_.toDouble)
        val x2 = point2(0)
        val y2 = point2(1)
        val pointsDistance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
        pointsDistance <= distance
    })

    val resultDf = spark.sql("select * from point where ST_Within(point._c0,'"+arg2+"',"+arg3+")")
    resultDf.show()

    return resultDf.count()
  }

  def runDistanceJoinQuery(spark: SparkSession, arg1: String, arg2: String, arg3: String): Long = {

    val pointDf = spark.read.format("com.databricks.spark.csv").option("delimiter","\t").option("header","false").load(arg1);
    pointDf.createOrReplaceTempView("point1")

    val pointDf2 = spark.read.format("com.databricks.spark.csv").option("delimiter","\t").option("header","false").load(arg2);
    pointDf2.createOrReplaceTempView("point2")

    // YOU NEED TO FILL IN THIS USER DEFINED FUNCTION
    spark.udf.register("ST_Within",(pointString1:String, pointString2:String, distance:Double)=>
    {
        val point1 = pointString1.split(",").map(_.toDouble) 
        val x1 = point1(0)
        val y1 = point1(1)
        val point2 = pointString2.split(",").map(_.toDouble)
        val x2 = point2(0)
        val y2 = point2(1)
        val pointsDistance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
        pointsDistance <= distance
    })
    val resultDf = spark.sql("select * from point1 p1, point2 p2 where ST_Within(p1._c0, p2._c0, "+arg3+")")
    resultDf.show()

    return resultDf.count()
  }
}

