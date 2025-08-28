namespace StablePerfectMatching;

using System;

class Program
{
    static void Main(string[] args)
    {
        
        
        string[] input = Console.ReadLine().Split(" ");

        int individuals = int.Parse(input[0]);
        int edges = int.Parse(input[1]);

        Queue<Person> unmatchedPeople = new Queue<Person>();

        for (int i = 0; i <= individuals; i++)
        {
            string[] preferenceInput = Console.ReadLine().Split(" ");
            
            unmatchedPeople.Enqueue(new Person(preferenceInput[0], preferenceInput[1..])); 
        }

        while (unmatchedPeople.TryDequeue(out Person? unmatchedPerson))
        {
            Console.WriteLine(unmatchedPerson);
        }
    }

    class Person(string name, string[] preferences)
    {
        public string Name { get; } = name;
        public string[] Preferences { get; } = preferences;
        public string PreferredPerson() => Preferences[0];
    }
}