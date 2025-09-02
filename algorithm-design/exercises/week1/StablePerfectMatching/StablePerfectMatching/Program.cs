
namespace StablePerfectMatching;

using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        string[] input = Console.ReadLine().Split(" ");
        
        int individuals = int.Parse(input[0]);

        Queue<Person> unmatchedProposers = new Queue<Person>();
        Dictionary<string, Person> rejectors = new Dictionary<string, Person>();
        

        for (int i = 0; i < individuals; i++)
        {
            string[] personInput = Console.ReadLine().Split(" ");
            Person person = new Person(personInput[0], personInput[1..]);

            if (i < individuals / 2)
            {
                unmatchedProposers.Enqueue(person);
            }
            else
            {
                rejectors.Add(person.Name, person);
            }
        }

        while (unmatchedProposers.TryDequeue(out Person? unmatchedPerson))
        {
            Person rejector = rejectors[unmatchedPerson.NextPreference()];

            if (rejector.PrefersPerson(unmatchedPerson))
            {
                if (rejector.Match != null && rejector.Match.HasPreferencesLeft())
                {
                    unmatchedProposers.Enqueue(rejector.Match);
                }
                
                rejector.Match = unmatchedPerson;
                unmatchedPerson.Match = rejector;
            }
            else if(unmatchedPerson.HasPreferencesLeft())
            {
                unmatchedProposers.Enqueue(unmatchedPerson);
            }
        }

        foreach (Person person in rejectors.Values)
        {
            Console.WriteLine(person.Match?.Name + " " + person.Name);
        }
    }

    class Person(string name, string[] preferences)
    {
        public string Name { get; } = name;
        public Person? Match { get; set; }
        public bool HasPreferencesLeft() => _preferences.Any();
        public string NextPreference() => _preferences.Dequeue();

        private List<string> _preferencePrecedence = new List<string>(preferences);
        private Queue<string> _preferences = new Queue<string>(preferences);

        public bool PrefersPerson(Person person)
        {
            if (Match is null)
            {
                return true;
            }
            
            int matchIndex = _preferencePrecedence.IndexOf(Match?.Name);
            int personIndex = _preferencePrecedence.IndexOf(person.Name);

            return personIndex < matchIndex && personIndex >= 0;
        }
    }
}