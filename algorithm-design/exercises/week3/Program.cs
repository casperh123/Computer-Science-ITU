using System;
using System.Collections.Generic;
using System.Linq;

int amountOfPoints = int.Parse(Console.ReadLine());

(double, double)[] points = new (double, double)[amountOfPoints];

for(int i = 0; i < amountOfPoints; i++) {
    string[] pointInput = Console.ReadLine().Split(" ");
    (double, double) point = (double.Parse(pointInput[0]), double.Parse(pointInput[1]));
    points[i] = point;
}

Array.Sort(points, (first, second) => first.Item1.CompareTo(second.Item1));

(double distance, (double, double) left, (double, double) right) closestPair = ClosestPair(points);

Console.WriteLine($"{closestPair.left.Item1} {closestPair.left.Item2}");
Console.WriteLine($"{closestPair.right.Item1} {closestPair.right.Item2}");

static (double distance, (double, double) left, (double, double) right) ClosestPair(Span<(double, double)> points)
{
    if (points.Length == 2)
    {
        return (Distance(points[0], points[1]), points[0], points[1]);
    }

    if (points.Length == 3)
    {
        double d01 = Distance(points[0], points[1]);
        double d02 = Distance(points[0], points[2]);
        double d12 = Distance(points[1], points[2]);

        if (d01 <= d02 && d01 <= d12) return (d01, points[0], points[1]);
        if (d02 <= d12) return (d02, points[0], points[2]);
        return (d12, points[1], points[2]);
    }

    int mid = points.Length / 2;

    (double distance, (double, double), (double, double)) leftSide = ClosestPair(points[..mid]);
    (double distance, (double, double), (double, double)) rightSide = ClosestPair(points[mid..]);
    
    (double x, double y) middlePoint = points[mid];

    (double distance, (double, double), (double, double)) closestPointPair =
        leftSide.distance <= rightSide.distance ? leftSide : rightSide;

    List<(double x, double y)> closestPoints = [];
    
    for (int i = 0; i < points.Length; i++)
    {
        (double x, double y) point = points[i];
        double distanceToMiddle = Math.Abs(middlePoint.x - point.x);

        if (distanceToMiddle <= closestPointPair.distance)
        {
            closestPoints.Add(points[i]);
        }
    }
    
    closestPoints.Sort((first, second) => first.Item2.CompareTo(second.Item2));

    for (int i = 0; i < closestPoints.Count; i++)
    {
        (double x, double y) point = closestPoints[i];

        for (int j = i + 1; j < i + 11 && j < closestPoints.Count; j++)
        {
            (double x, double y) comparingPoint = closestPoints[j];
            double distance = Distance(point, comparingPoint);

            if (distance < closestPointPair.distance)
            {
                closestPointPair = (distance, point, comparingPoint);
            }
        }
    }
    
    return closestPointPair;
}

static double Distance((double, double) first, (double, double) second)
{
    double dx = first.Item1 - second.Item1;
    double dy = first.Item2 - second.Item2;
    return dx * dx + dy * dy;
}