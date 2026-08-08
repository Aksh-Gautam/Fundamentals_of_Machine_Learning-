Machine Learning 

ML tells a computer to learn from data recognise patterns and make its own decision without any explicit instructions from humans. 

Types:
—> Supervised learning: A model is trained on labeled data (Input/Output parameters given)
—> Unsupervised learning
—> Semi-supervised learning *(SSL models train on labeled data)
—> RLHF (reinforced learning from human feedback)

Machine Learning Pipeline:

``` mermaid
flowchart TD
    A[Model Pipeline] --> B[Data Creation]
    B --> C["Splitting Features / Targets"]
    C --> D["Splitting Train / Test"]
    D --> E[Model Creation]
    E --> F[Model Training]
    F --> G[Model Evaluation]
    G --> H[Deployment]
```

