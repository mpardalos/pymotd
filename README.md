A python Message of the Day script. Configure it through the parameters passed
to the get_motd function in the `if __name__ == '__main__'` section at the end of
the file, or, if you are so inclined, by importing this file and calling the
get_motd function yourself. 

In this default configuration, it prints a message similar to this:

```
I surely do hope that's a syntax error.
             -- Larry Wall in <199710011752.KAA21624@wall.org>

      /#\
     /###\
    /p^###\
   /##P^q##\
  /##(   )##\
 /###P   q#,^\  Linux TARDIS 4.10.9-1-ARCH 
/P^         ^q\  7 updates available 
```

The Arch ASCII image is not hardcoded, but is rather loaded from ~/.motd_image
(this can be changed). More messages can also be added and the fortune message
at the top can be swapped out for something else or removed entirely. 
