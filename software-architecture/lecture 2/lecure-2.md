# Lecutre 2 notes

## 3 + 1 Model

Consists of 3 concrete viewpoints. Views are concrete architectural desciprtions.
This is the minimal amount of views one should have, but it is only a MVP with these 3 views.

The three viewpoints are:

- Module viewpoint -> Describes how functionality maps to static development units.
    - Basically the runtime view. What does the software look like when its running?
- Component & Connector viewpoint -> Runtime mappings of functionality to components of the architecture
    - Runtime view.
    - Explain wich kind of connections there are. Architectural patterns should not be described here.
- Allocation viewpoint -> How software entities are mapped to environmental (real?) entities.
    - Deployment view.
    - Environmental nodes. Hardware and firmware that our system sits upon (if relevant)
    - Respects the real count of the devices, servers, terminals etc. Annotate with amount.

Futhermore we have the __mission__ of the system, which is the collection of the systems significant requirements.

## 3 + 1 In UML

UML can be used for (architectural) design documentation
- Module view: class diagrams with packages and classes
- C&C view: class diagrams with objects and links, sequence diagrams
- Deployment view: deployment diagram with nodes and components

## Reasons to architect

Ensure we are resolving the right problem. 
Ensure that we are doing things right.
Help us ensure we are not forgetting anything by visualising the problem.

## Terms

- __Box-and-line diagram__: Random diagram, that do not conform to any standardized way of construction
- View: Diagram with a unique perspective on the system. *Represents a aprtial aspect of the software.
- Dynamic view: Runtime view
- Static view: Design time view
- ADL (Architectural Description Language)  

