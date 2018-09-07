# watson_chatbot
creating a watson chatbot using IBM watson services for a flower shop

# Do's and Don'ts
In terms of a good chatbot design there are three fundamental rules that you should follow

**First Rule**

Avoid using **YES** or **NO** in your replies

If your chatbot fails to interpret the question, a **yes** or **no** answer would be 
misleading or provide wrong information.

**For example:**

We might set the reply for a question that asks for 

```
Q. Is delivery free?
A. Yes! it is
```

But what happens when the question is changed slightly

```
Q. Is delivery free or do I have to pay for it?
A. Yes! it is
```

The same answer won't work here. This situation arrived because of the negatives included 
in the question, where a human would answer **no** our chatbhot ends up answering **yes**

It would be far better to provide an answer that covers the topic of delivery price, 
without including an element of **yes** or **no** in it.

**Correct Reply**

```
Q. Is delivery free or do I have to pay for it?
A. Deliveries are free.
```

**Second Rule**

**Incorporate part of user's question in your response whenever possible**

For example, say 

```
A. "I understand that you’re looking for help with an order.
	Unfortunately, I'm unable to look into orders that have already been placed."
```
And then perhaps we would have the chatbot refer the customer to our phone number or
email address, in order to help them perhaps speak with a live person about their concern.
This will further cement, in our user's mind, the relative intelligence of our chatbot,
even though it technically failed to directly provide what the customer was hoping to find
out.

**Third Rule**

**Succinct and accurate answers are the best**

This means we want to be informative but not reply with a wall of text. So we should keep 
our answers short. When a wall of text is an absolute must, to convey the information,then 
deflecting by sending the user to an informative page is a better approach.

# Creating Watson Chatbot
1. **Register** with Watson Assistant by clicking on this link.

2. **Verify your account** by clicking the confirmation email you receive by email (be 
sure to check your spam folder, if you don't see the email).

3. **Log in to IBM Cloud** (which hosts the Watson Assistant service) and when prompted, 
chose a cloud region and create an organization and space. US-South will work for many, 
but you have the option to select other cities and countries. For the organization, you 
can use your company name or even your own name. For space, pick a namespace that makes 
sense to you. For example, it can be a department in your organization (e.g., marketing) 
or a phase of development (test, dev, staging, or prod). You'll be able to customize and 
add new regions, organizations, and spaces at any time, so don't worry too much about 
what you select at first.

4. **Click on the Assistant service** within the Watson portion of the IBM Cloud 
catalog. 
This will bring you to a service creation page where you'll be asked to enter a name for 
the service. You can enter whatever you like or simply **watson-assistant-flower-shop**
Select the Lite plan that offers you up to 10,000 requests per month for free and click 
on **Create** Click on the Launch tool to launch the Watson Assistant user interface.

5. **Click on the workspace** to create any workspace or click on the existing one, and 
explore the example chatbot. What intents and entities are there? If you are adventurous 
you can even take a look at the dialog section. Play around with the default example in 
Watson Assistant and when you feel like you have become more familiar with it, go back 
to the workspaces list by clicking on the table icon in the left side of the page.

# Creating Workspace
Once we have our watson assistant ready, go to the workspace page again and click on
**Create Workspace** You will be asked for a name, I named it ```Florence Chatbot```
then enter the description for my case I used 

```
Flower Shop Chatbot for providing assistance in flower suggestions and delivery 
information.
```

Choose your preferred language for chatbot and **Create**.

The redirected page opened says to **Create Intents** because our chatbot currently has
no intents defined. On the top right corner click on **Try it out**, this is where you
can test your chatbot after each progress. You can enter in any message to chatbot.

Let's enter ```hello``` and we have no response and the bar under our message is also
empty, the bar will display the intent of the message.

# Create Intent
On the Intent page click on **Add Intent** and a form appears, name your intent 
```greetings``` and add in description like ```greet the user``` and in the 
```Add user examples``` add the examples of greetings.

For example

```
hello
hi
hey
hey there
what's up
how you doing
good morning
good evening
greetings
nice to see you
...
```

You can add as many intents you like based on many ways a user might greet our bot.
Once added intents you might see that ```Try it out``` says ```Watson is training```

That meas our Watson assistant is training and once that message goes we can test our 
chatbot by sending user examples we have set as well as any related random messages
we haven't trained our bot with.

Once message is entered our chatbot should identify the intent of the message and 
display it under the message

The same way create intents for ```#thank_you``` and ```#goodbyes```

**NOTICE** how I wrote ```thank_you``` because intent name cannot have spaces in it

Since we are making a chatbot assistant for a flower shop we would need more
intents than just ```greetings``` and ```goodbyes```

**Create** intents for ```#flower_suggestions``` and ```#delivery_info``` 

If a user asks for flower suggestions or flower recommendations then 
```#flower_suggestions``` intent will be avoked and if asks for delivery information
the ```#delivery_info``` intent will be activated

Some user examples are

**#flower_suggestions**
```
bouquet for girlfriend
flower recommendations
flowers for anniverseries
flowers for a yound lady
flowers for friend
flowers for judges
flowers for marriage function
flowers for my aunt
flowers for my uncle
flowers for your daddy
flowers for your father
flowers for your mother
flowers for your soulmate
flower suggestions
glowers for anniverseries
I'd like to buy some flowers for a sick friend
i want a bouquet for my wife
i want flower for award ceremony
i want flowers for funeral
i want flowers for marriage function
i want flowers for my gf
i want flowers for my loved ones
i want flowers for wedding gift
I want flowers that express sympathy
i want to send flowers to my friend
recommend arrangement of flowers for gettogether
recommend arrangement of flowers for relatives
recommend best flowers for award ceremony
recommend best flowers for award function
recommend best flowers for chief guest welcome
recommend flowers for date
recommend me flowers
suggest best flowers for valentines day
suggest flowers for a date
suggest flowers for award ceremony
suggest flowers for funeral
suggest flowers for girl
suggest flowers for greeting chief guest
suggest flowers for honouring chief guest
suggest flowers for teachers day
suggest flowers for wedding
suggest flowers for wedding function
suggest some nice flowers
what kind of flowers
what should be a good arrangement to give someone when they're retiring
which flower for a birthday
which flower for a funeral
which flower should i buy
which type of flowers are good choice as anniversery gift for your parents
which type of flowers are good choice when meeting someone
which variety of flowers do you have
...
```

**#delivery_info**
```
Do you deliver
do you deliver during holidays
do you deliver on weekends
how do i get my flowers
how much is delivery expenses
how much time in delivery
how will you deliver
is delivery free
what do ou deliver
when do you deliver
when will I get my delivery
when will i get my flowers
when will i receive my flowers
when will you deliver
will i be able to get my flowers on sundays
...
```

There can be lots and lots more of user examples and even mistakes in spelling from
the user side so the **more the examples better the assistant** gets trained.
