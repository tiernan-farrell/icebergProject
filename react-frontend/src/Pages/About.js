export default function About(){
    return (
        <div className='about'> 
            <h1 id="icebergproject">icebergProject</h1>
            <p>This project was created by group 5 in CSE 5242.  The goal of this project
            is to create a web interface where a user can choose between a set of iceberg cubing 
            algorithms and examine the difference in execution time for different sets of data.</p>
            <h2 id="initial-setup">Initial Setup</h2>
            <p>Before the web interface is built and real data sets are found/created, the algorithms
            will be implemented and tested using python generated data in the form of a .txt file.  
            The data will be pre-processed and the algorithms will be implemented using the processed data.</p>
            <h3> Data Generation: </h3>
            <p><code>dataGenerator.py</code> generates 10000 tuples of data where each 
            tuples contains 5 random integers from 0-9. using the command
            <pre><code><span class="hljs-selector-tag">python3</span> <span class="hljs-selector-tag">dataGenerator</span><span class="hljs-selector-class">.py</span> &gt; <span class="hljs-selector-tag">data</span><span class="hljs-selector-class">.txt</span></code></pre>
            pipes the ouptut from the data generator into a usable text file</p>
            <h1 id="dependencies">Dependencies</h1>
            <pre><code> -<span class="ruby">python version <span class="hljs-number">3.10</span>.<span class="hljs-number">6</span>
            </span>    -<span class="ruby">pip version <span class="hljs-number">22.3</span>
            </span>    -<span class="ruby">venv
            </span>    -<span class="ruby">npm 
            </span>    -<span class="ruby">flask
            </span>    -<span class="ruby">flask-cors</span>
            </code></pre>
            <h1 id="web-interface">Web Interface</h1>
            <p>To run the front end application, start a pyhon server and a http-server 
            use: &nbsp;
                <code>$python3 buc.py</code> 
            &nbsp; in the directory of the main project to start the python backend server 
            </p>
            <p>To start the frontend server, use: &nbsp; 
                <code>$cd react-frontend</code> &nbsp;
                <code>$npm start</code> &nbsp;
            in the /frontend directory. Navigate to the server that was started at 
                <code>http://localhost:3000</code>.
                &nbsp; From here you can click the buttons to show you the data used and then the buc iceberg cube. </p>


            <h1 id="algorithms">Algorithms</h1>


            <h2 id="buc-bottom-up-computation-">BUC (Bottom Up Computation)</h2>
            <li>Bottom up computation is a method in which the database is repeatedly sorted and partitioned
            and only values that meet the minimum support are kept. This starts at the &quot;bottom&quot;
            of the cube lattice and begins the sort only on the first attribute. Only the values for the
            first attribute that are above the min support level are partitioned. BUC then recursively calls
            itself reducing the input table to the partitioned table and increasing the starting dimension.
            BUC climbs up the lattice in this manner pruning out groups that don&#39;t meet minsup, then eventually
            comes back down to repeat on the next partition and so on.
            </li>
            <ol>
                <li>Sort database on attribute d=0</li>
                <li>If an attribute value meets minsup, recursively call the buc algorithm with the dimension incremented and input table as only those tuples with the current value for current dimension.</li>
                <li>If it does not meet minsup we prune it and dont add the counts to iceberg cube.</li>
                <li>Recursion continues up the lattice and checks all combinations of attributes at each level to see if they are above minsup.</li>
                <li>Sort database on attribute d+1 and repeat until d=number of dimensions</li>
            </ol>
            <img width="458" alt="image" src="https://user-images.githubusercontent.com/63930496/197000331-6d14ecf9-54b7-4ba5-91b2-aadec6bb0bcd.png"></img>       

            <p>For this cube lattice, the processing tree of the buc algorithm looks like this:</p>
            <img width="458" alt="image" src="https://user-images.githubusercontent.com/63930496/197291959-e3b5ee17-c59c-49d8-abd0-84daad4979cd.png"></img>

            <p>Where the number next to the region in the lattice represents the order it is processed by BUC.

            BUC climbs the lattice recursively then decends downward. Notice all of dimension A was processed before dimension B starts.</p>
            
            <h2>Top-Down Computation</h2>
            <ul>
            <li>Top Down Computation computes the iceberg cube in top down fashion of the lattice. 
            If there are 4 dimensions ABCD, TDC loops over the input first counting combinations of 
            ABCD, ABC, AB and A. Then it continues looping checking regions in the order: ABD, ACD, AC, BCD, BC, B, CD, CD, C, D, ALL. </li>
            <li>With n dimensions there are <code>2^n-1</code> combinations and TDC makes as many passes over the input. </li>
            <li>Pruning can happen if no attribute value combinations are found frequent.</li>
            <li>Traverses lattice the opposite of BUC with the same recursive and iterative structure.</li>
            </ul>

            <h2>APRIORI</h2>
            <ul>
                <li>Apriori functions utilize candidate combinations in order to prune useless attribute value combinations.  It follows the Apriori Property which states “All non-empty subsets of a frequent itemset must be frequent”.  Therefore, for a combination of attribute values to satisfy the minimum support requirement, all subsets of that combination must also satisfy minimum support.  Apriori uses this property by only allowing candidate combinations that are combinations of frequent attribute value combinations.  Apriori starts looking at one value on the first pass of the data, then considers all candidate combinations of the frequent single values and looks at the two value combinations on the second pass of the data.  The data is continually passed until either all combinations are pruned or the number of values in the candidate combinations after being passed through is equal the original dimensionality of the data.</li>
                <li>This can best be seen with the example below:</li>
                <img width="458" alt="image" src="images/Apriori.png"></img>
                <li>Supposing the input table 4, on the first pass of data, Apriori determines that single values in Table 5 are frequent.  Table 6 shows the candidate combinations that result from the combinations in Table 5.  The candidate combinations are then passed through, resulting in the cominbations and counts seen in Table 7.  3-set candidates are then generated for the candidate combinations as seen in Table 8, and then passed through resulting in Table 9.  Since  (a2, c2, d2) is not frequent no more candidate combinations can be derived, so the algorithm finishes executing.</li>
            </ul>

        </ div >
    );
}