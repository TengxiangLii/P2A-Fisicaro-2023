# Principles of isomer stability in small clusters†

Giuseppe Fisicaro,*<sup>a</sup> Bastian Schaefer,<sup>b</sup> Jonas A. Finkler<sup>b</sup> and Stefan Goedecker<sup>b</sup>

Published on 28 February 2023. Licensed under CC-BY 4.0

Cite this: _Mater. Adv._, 2023, 4, 1746

In this work we study isomers of several representative small clusters to find principles for their stability. Our conclusions about the principles underlying the structure of clusters are based on a huge database of 44 000 isomers generated for 58 different clusters on the density functional theory level by Minima Hopping. We explore the potential energy surface of small neutral, anionic and cationic isomers, moving left to right across the third period of the periodic table and varying the number of atoms _n_ and the cluster charge state _q_ (X<sub>_n_</sub><sup>_q_</sup>, with X = {Na, Mg, Al, Si, Ge}, _q_ = −1, 0, 1, 2). We use structural descriptors such as bond lengths and atomic coordination numbers, the surface to volume ratios and the shape factor as well as electronic descriptors such as shell filling and hardness to detect correlations with the stability of clusters. The isomers of metallic clusters are found to be structure seekers with a strong tendency to adopt compact shapes. However certain numbers of atoms can suppress the formation of nearly spherical metallic clusters. Small non-metallic clusters typically also do not adopt compact spherical shapes for their lowest energy structures. In both cases spherical jellium models are not any more applicable. Nevertheless for many structures, that frequently have a high degree of symmetry, the Kohn–Sham eigenvalues are bunched into shells and if the available electrons can completely fill such shells, a particularly stable structure can result. We call such a cluster whose shape gives rise to shells that can be completely filled by the number of available electrons an optimally matched cluster, since both the structure and the number of electrons must be special and match. In this way we can also explain the stability trends for covalent silicon and germanium cluster isomers, whose stability was previously explained by the presence of certain structural motifs. Thus we propose a unified framework to explain trends in the stability of isomers and to predict their structure for a wide range of small clusters.

Received 18th December 2022, Accepted 28th February 2023

DOI: 10.1039/d2ma01088g

rsc.li/materials-advances

## I. Introduction

The physics of small clusters composed of a few to some hundred atoms represents an intriguing field of science. The physical and chemical properties of such clusters differ not only considerably from the properties of isolated atoms and bulk materials<sup>1–4</sup> but can also vary considerably with the number of constituent atoms.<sup>5–8</sup> The addition/removal of a single atom<sup>5</sup> or a single electron<sup>9</sup> may for instance lead to different ground state geometries. Different structures can then lead to completely different properties. Gold clusters that consist of a certain number of atoms can for instance exhibit catalytic activity.<sup>10</sup> This high variability of cluster properties results in a lot of opportunities to create clusters with certain desired properties. Such clusters can then also be used as building blocks for cluster-assembled materials with certain desired properties.<sup>11–18</sup> Fullerenes<sup>19</sup> and their assembly in fullerides<sup>20,21</sup> are a prominent example. Alkali doping of fullerides raises for instance the superconducting transition temperature of the cluster-based material by more than one order of magnitude.

Clusters can in principle be made of any number of atoms. The inspection of experimental mass spectra shows however that clusters of certain sizes can be found much more frequently than other sizes. For these sizes particularly low geometric ground states can be formed and they are called magic sizes. Numerous publications on the topic exist. We will extend the scope of these investigations by not only identifying geometric ground states as candidates for magic sizes, but by proposing general principles that also explain the relative stability of meta-stable isomers of clusters independently of whether they are magic sizes or not.

<sup>a</sup> Consiglio Nazionale delle Ricerche, Istituto per la Microelettronica e Microsistemi (CNR-IMM), Z.I. VIII Strada 5, I-95121 Catania, Italy. E-mail: Giuseppe.Fisicaro@imm.cnr.it

<sup>b</sup> Department of Physics, University of Basel, Klingelbergstrasse 82, CH-4056 Basel, Switzerland

† Electronic supplementary information (ESI) available: The file supplementary-information.pdf reports two additional analyses concerning the redistribution of the electronic charge density for selected Na and Mg clusters together with various figures from the main publication augmented by the data used to make the figure plus selected structural and electronic properties. See DOI: https://doi.org/10.1039/d2ma01088g

Two basic types of theories exist to explain the particular stability of clusters with magic sizes. The first theory is just based on purely geometrical considerations, while the second is based on the filling of electronic shells in a spherical jellium model.

For a simple pairwise potential icosahedral structures are highly stable. The smallest stable icosahedron can be formed by the 12 atoms located at the 12 corners of the icosahedron plus a central atom. The next two icosahedral structures then have one or two additional shells of atoms and consist of 55 and 147 atoms. So according to this geometrical theory the sizes containing 13, 55 and 147 atoms are predicted to be magic. Experimentally these sizes turn out to be magic sizes for rare gas atom clusters that are weakly interacting by van der Waals forces.<sup>22,23</sup>

The second theory establishes a connection between the number of valence electrons in the cluster and its stability. The concept of cluster electronic shells and the enhanced stability of clusters with completely filled shells starts from the work of Knight and co-workers on magic numbers in the mass spectra of free small sodium clusters.<sup>24</sup> They detected a particular high stability for clusters containing 2, 8, 18, 20, 34, 40, 58. . . atoms. Knight and co-workers succeeded in rationalizing the experimental observations by means of the jellium model.<sup>25–27</sup> The jellium model, an extension of the independent nuclear shell model,<sup>27</sup> assumes that a gas of independent electrons is spatially confined by a model potential within a sphere. A uniform positive background charge mimics the ions in the cluster. The quantum mechanical energy levels of such a system together with their electronic occupations are given by |1s<sup>2</sup>|1p<sup>6</sup>|1d<sup>10</sup>|2s<sup>2</sup>|1f<sup>14</sup>|2p<sup>6</sup>|1g<sup>18</sup>|. . ., where s,p,d denote in the usual way the values _l_ = 0, 1, 2 of the angular quantum number. The energetic ordering of the energy levels of electrons is however different from the one for a Coulombic potential. For most flat potentials<sup>27</sup> the degenerate shells of jellium clusters can accommodate 2, 8, 18, 20, 34, 40, 58. . . electrons. Clusters with this number of valence electrons are considered _magic clusters_ in this electronic theory.

For Na clusters it has been observed that for small sizes of up to 1500 atoms magic sizes are determined by electronic shell filling, whereas for larger sizes it is determined by complete geometrical shells.<sup>28</sup> For the small clusters we are studying geometrical shell filling is in general not possible and only the Al<sub>13</sub><sup>−1</sup> and the Al<sub>12</sub>Si exhibit this effect since they have a completely filled icosahedral shell.

Various generalizations of the jellium model have been proposed that take into account deviations from spherical symmetry. Distortions of the spherical shape lead to a splitting of energy levels with different quantum numbers, _l_.<sup>29</sup> For weak distortions, the splitting is however relatively small<sup>30</sup> so that they still can be lumped together into the levels of a spherical potential. Many of the early works on non-spherical metal clusters<sup>26,31,32</sup> were not based on systematic structure predictions at the density functional theory (DFT) level. Since only this approach can reliably find the ground state geometries, it is therefore questionable whether the assumed shapes and resulting properties were the correct ones. Distorted jellium models fail for instance to predict the icosahedral shape of the Na<sub>55</sub> cluster that is obtained from DFT calculations.<sup>33</sup> The jellium model and its generalizations work best for clusters made out of alkaline and alkaline earth metals. As soon as atomic p orbitals come into play, such as in Al clusters, a jellium like shell structure is absent in most cases.<sup>34</sup> It should also be pointed out that the jellium model fails for transition metal clusters.<sup>35</sup>

Trends in cluster properties are related according to the jellium model to the occupation of molecular electronic shells in much the same way as the occupation of the atomic shells govern the properties of the elements in the periodic table. This suggests that it is possible to regard particular clusters as superatoms.<sup>11,13,16,36–38</sup> The concept of magic clusters paves the way to superatoms physics. Following the findings on the halogen character of the Al<sub>13</sub> cluster, various research groups, such as the experimental group of Castleman and Khanna’s theory group<sup>12,13,39</sup> explored the concept of superatoms. For instance, adding an electron to the 39 valence electrons of the neutral cluster leads to a fully occupied shell of the jellium model. This leads to a high electron affinity of 3.6 eV which is comparable to that of the chlorine atom. Therefore, the cluster behaves in a similar way to an halogen atom.<sup>11,36,40,41</sup>

We propose in this study a theoretical framework which goes beyond the jellium model. It is based on geometrical arrangements of the nuclei that lead to electronic shells that can be filled completely by the number of available electrons. These shells are however in general quite different from the shells predicted by the jellium model as well as its extensions. In contrast to any kind of jellium model we do not have to assume that the nuclei are completely smeared out into a uniform background charge, but we can use real point like nuclei. Our approach is also not restricted to explain the stability of magic size ground states, but can explain the stability of any cluster.

In order to substantiate our model we explore and analyse the potential energy surface (PES) of various neutral and charged cluster isomers at the density functional theory level. The clusters are made out of elements of the third period of the periodic table and span the groups I to IV. In this way we can compare the behaviour of metallic and covalently bonded clusters. To understand the general principles of cluster stability we do not only consider systems that are experimentally known to be magic sizes. Instead we study in general the influence of the variation of the number of atoms and electrons on low energy meta-stable isomers. We do not consider in this work transition metal clusters. So if we refer in the following to metals we mean simple metals.

## II. Methods

The minima hopping (MH) method<sup>42</sup> was employed to systematically explore the potential energy surface of all clusters being studied. For every cluster several runs, starting from different initial structures, were performed. The runs were stopped when the clusters started to fragment frequently due to a high temperature of the molecular dynamics escape trajectories. Since the temperature is increased whenever a minimum is revisited, this indicates that a large fraction of all metastable structures has been found. Within MH, consecutive short molecular dynamics simulations are performed to escape from the local minima, followed by local geometry optimizations to efficiently sample the energy landscape. The initial velocities of the molecular dynamics escape trials are preferably aligned along low curvature modes of the local minima to exploit the Bell–Evans–Polanyi principle.<sup>43,44</sup> A feedback mechanism based on a search history discourages revisiting already known local minima, allowing fast exploration of large portions of the PES. The transition states between the local minima on the PES were explored using the minima hopping guided path search with the stabilized quasi-Newton saddle optimizer.<sup>45,46</sup>

All structural searches were performed directly at the Kohn–Sham (KS) density functional theory level by coupling the MH method with the BigDFT package.<sup>47–49</sup> BigDFT uses wavelets as basis functions, which are localized both in real and Fourier space and allows for an exact treatment of free boundary conditions without the need to introduce vacuum regions in the periodic dimensions for both neutral and charged systems. As a consequence, the code is well suited for the evaluation of the KS energies and forces for neutral and charged isolated clusters. Soft norm-conserving pseudo-potentials including non-linear core corrections<sup>50,51</sup> were used. Except for Mg where we have used for backward compatibility<sup>7</sup> the Local Density Approximation, the Perdew–Burke–Ernzerhof functional<sup>52</sup> as implemented in the Libxc<sup>53</sup> library was used. Spin polarized calculations were performed for all the clusters with an odd number of electrons. For a cluster with an even number of electrons, it was assumed that the electronic ground state is a singlet state, even though some exceptions to this rule are known.<sup>54</sup> A zero electronic temperature was used for all the calculations, except for the Mg clusters with an odd number of electrons where a temperature of 3 × 10<sup>−3</sup> Ha was used for faster convergence. All structures were relaxed using the Hellman–Feynman scheme until forces were less than 0.5 meV Å<sup>−1</sup>. We have made all data generated by this research, that are all structure coordinates of all minima found by the minima hopping method together with their structural and electronic properties, openly-available through the Materials Cloud Archive.<sup>55</sup>

## III. Results and discussion

Table 1 reports various structural and electronic properties of all global minima found by the MH method for all investigated systems. For the 58 different neutral and charged clusters listed in column 1 of Table 1 (we moved left to right across the third period of the periodic table varying the number of atoms _n_ and the cluster charge state _q_, that is X<sub>_n_</sub><sup>_q_</sup>, with X = {Na, Mg, Al, Si, Ge}, _q_ = −1, 0, 1, 2), we found in total about 44 000 different minima on the potential energy surface of all these clusters. The global minimum (GM) gives the geometric ground state of the cluster whereas the local minima correspond to meta-stable structures.

Our global minimum structures for various cluster families are in agreement with previous structure prediction searches and experimental investigations. They are all shown in Fig. 1. The global minimum of Na<sub>8</sub> agrees with previous Car–Parrinello simulations,<sup>58</sup> the Na<sub>10</sub><sup>−1</sup> and Na<sub>15</sub> GMs agree with the GM structures found by means of the CALYPSO structural search coupled to the simulated photoelectron spectra.<sup>59</sup> Magnesium neutral global minima agree with the ones found by the CALYPSO structure prediction code<sup>60</sup> and with other DFT studies.<sup>61–63</sup> Global minima for neutral and charged aluminium clusters agree with previous DFT calculations for Al<sub>7</sub>.<sup>64,65</sup> All the global minima of aluminum clusters match the ones determined by means of a multistage search approach (genetic algorithm, basin hopping, minima hopping and ‘‘by hands constructions’’).<sup>66–68</sup> Silicon global minima agree with the one determined by infrared multiple phonon dissociation spectra.<sup>69</sup> Si<sub>15</sub> GM corresponds to the one found by genetic algorithm explorations coupled to ion mobility measurements<sup>70</sup> and the one determined by vibrational IR spectra coupled to DFT calculations.<sup>71</sup> Si<sub>20</sub> GM agrees with the one found by single-parent evolution search,<sup>72</sup> the one determined by the ‘‘big bang’’ optimization method<sup>73</sup> or with previous MH structure predictions.<sup>9</sup>

### A. Structural properties

To analyse the structural properties of the cluster isomers we have introduced several descriptors for the geometric shape of these clusters, namely the average coordination number and bond distance, the surface to volume ratio, the shape factor and the fingerprint distance to the global minimum.

**1. Average coordination number and bond distance.** The coordination number _ζ_<sub>_k_</sub> of an atom _k_ equals the number of atoms within the first coordination shell. We define the first coordination shell by a soft cutoff that decreases continuously from one at the nearest neighbor distance _τ_ to zero at the second nearest neighbor distance _ν_. These nearest neighbor and second nearest neighbor distances _τ_ and _ν_ were extracted from the elemental crystalline ground state bulk structures<sup>57</sup> and are given (in Å) by: τ<sub>Na</sub>: 3.633, τ<sub>Mg</sub>: 3.204, τ<sub>Al</sub>: 2.856, τ<sub>Si</sub>: 2.386, τ<sub>Ge</sub>: 2.495 and ν<sub>Na</sub>: 4.195, ν<sub>Mg</sub>: 5.240, ν<sub>Al</sub>: 4.039, ν<sub>Si</sub>: 3.867, ν<sub>Ge</sub>: 4.075. The coordination number _ζ_<sub>_k_</sub> for an atom _k_ in a cluster is then given by

$$\zeta_k = \sum_{l=1}^{n} \zeta_{kl}, \qquad (1)$$

_n_ being the total number of atoms in the cluster. The contribution _ζ_<sub>_kl_</sub> of atom _l_ is

$$\zeta_{kl} = \begin{cases} 1 & \text{if } d_{kl} < \tau_\mathrm{X} \\ (2\kappa+1)\times(\kappa-1)^2 & \text{if } \tau_\mathrm{X} < d_{kl} < \nu_\mathrm{X} \\ 0 & \text{if } \nu_\mathrm{X} < d_{kl} \end{cases} \qquad (2)$$

where _d_<sub>_kl_</sub> is the distance between the _k_ and _l_ atoms, and _κ_ = (_d_<sub>_kl_</sub> − τ<sub>X</sub>)/(ν<sub>X</sub> − τ<sub>X</sub>). By construction the _ζ_<sub>_k_</sub> is identical to the number of nearest neighbors in the bulk structure.

**Table 1** Structural and electronic properties of all global minima found for all neutral and charged clusters. The point group degeneracies are the symmetry-allowed orbital degeneracies<sup>56</sup>: 1 means that no symmetry related degenerate orbitals exist; an _n_ > 1 means that an _n_-fold degenerate orbital can be present. The degeneracy of the calculated KS orbitals is also listed. Starred numbers indicate approximate degeneracies. Rows in bold highlight clusters with a magic number of electrons according to the jellium model. The nearest neighbor bond distances _τ_, extracted from the elemental crystalline ground state bulk structures,<sup>57</sup> are given (in Å) by: τ<sub>Na</sub>: 3.633, τ<sub>Mg</sub>: 3.204, τ<sub>Al</sub>: 2.856, τ<sub>Si</sub>: 2.386, τ<sub>Ge</sub>: 2.495

_Conversion note: in the CSV, cluster names are written as X<n>^<charge> (e.g. Na8^-1 = Na<sub>8</sub><sup>−1</sup>), point groups as plain text (D2d = D<sub>2d</sub>), and the last column "Bold in source" marks the rows printed in bold (jellium magic electron count)._

[Table 1](../assets/table/table-1.csv)

[Fig. 1](../assets/figure/figure-1.jpg)

**Fig. 1** The structures of all global minima are shown together with their symmetry point groups and their electronic densities of states. The vertical dashed line on each global minimum DoS represents the Fermi level. The panels on the left of the structures show the KS energies _E_<sub>KS</sub>−_E_<sub>KS</sub><sup>0</sup> of the energetically sorted lowest 100 meta-stable structures with respect to the ground state, as a function of the sorting index for neutral and ionized clusters. If this function is rising rapidly, the energy increases strongly from one structure to the next energetically higher one.

The average coordination number _ζ_ associated to a particular isomer is the average of _ζ_<sub>_k_</sub> over all atoms _k_. The average bond distance is defined as the average over all atoms _k_ of a cluster isomer of the average over all distances between the _k_ atom and all the other atoms _l_ used in the calculation of the coordination number _ζ_<sub>_k_</sub>.

[Fig. 2](../assets/figure/figure-2.jpg)

**Fig. 2** Correlation between the Kohn–Sham energy _E_<sub>KS</sub> of isomers and their average coordination number _ζ_. Each sub-box belongs to a particular cluster family. _E_<sub>KS</sub><sup>0</sup> is the KS energy of the global minimum. The color scale for data dots is based on the average bond distance (Å). The red dot represents the global minimum for each PES.

Fig. 2 shows the correlation between the Kohn–Sham energy _E_<sub>KS</sub> and the average coordination number _ζ_. Each sub-box is associated to a particular cluster family. The color scale for data dots indicates the average bond distance. The red dot represents the global minimum for each particular PES.

We notice a remarkable and nearly linear correlation between the Kohn–Sham energy _E_<sub>KS</sub> of the isomers and their average coordination number _ζ_ for all examined simple metals. The global minima of all the metallic systems are characterized by a high average coordination number _ζ_ with a value higher than five or six depending on the cluster size _n_. Even though, as already pointed out, we do not study transition metal clusters, let us add for completeness that our findings for simple metals clusters are certainly not transferable to transition metal clusters. As is well known both pure<sup>74</sup> as well as decorated<sup>75</sup> small gold clusters have for instance planar shapes.

For the non-metallic clusters, where directional covalent bonds dominate, no such correlation can be seen. Like the corresponding bulk materials, the metallic clusters have much larger coordination numbers than the non-metallic clusters.

Table 1 reports the average bond distance of all global minima found in our minima hopping runs for neutral and charged clusters. In all cases the global minima of metallic clusters (sodium, magnesium and aluminium) have a shorter average bond length than the bulk phases. This is due to a redistribution of the charge from the region outside the surface of the cluster to the centers between neighboring atoms in the cluster as can be seen from the panels in the second row in Fig. 3, corresponding to an isovalue of 0.004. This charge redistribution is possible in a metallic system and leads to a lowering of the energy since the additional electronic charge inside the cluster is fully surrounded by the positively charged nuclei, whereas outside the surface it would only interact with a much smaller number of surface nuclei. A higher charge density in between neighboring atoms leads accordingly to the Hellmann–Feynman theorem to shorter bond lengths. This mechanism, which leads to bond shortening, is also encountered for the clusters of the other two elements that we examined, namely Na and Mg, as shown in Fig. S1 and S2 of the ESI.†

Apart from this charge flow towards bond centers, the bonding properties of the elemental metallic solid and the cluster are quite similar. As can be seen from the top panels in the first row of Fig. 3 (isovalue 0.002), there is a ring shaped electronic cloud around the atoms with a peak in the middle between nearest neighbors.

[Fig. 3](../assets/figure/figure-3.jpg)

**Fig. 3** The difference between the selfconsistent DFT charge density and the sum of the atomic charge densities of spherically symmetrized atoms. For each isovalue only the positive part is shown which illustrates the flow of the electronic charge density when the structure is formed out of individual atoms. Top row shows the charge difference at an isovalue of 0.002 for Al<sub>13</sub><sup>−1</sup> and bulk fcc aluminum. The non-directional character of the bonding is clearly visible. In the panels of the second row a large isovalue of 0.004 was chosen to make the charge flow towards the center of the Al<sub>13</sub><sup>−1</sup> cluster visible. Bottom panels in the third row show the charge difference at an isovalue of 0.006 for the Si<sub>10</sub> cluster and bulk silicon. The yellow blobs in the bulk silicon, representing the charge accumulation, are centered exactly in the middle of the bonds. This accumulation in the middle of all the bonds is not possible anymore in the cluster.

On the other side, the global minima of the covalent systems (silicon and germanium) are characterized by larger average bond distances compared with the corresponding bulk materials. Due to the strong directional bonding in insulators arising from hybridized orbitals, the charge in a disordered structure cannot flow into the bond region between two atoms to the same extent as in a solid with a perfect tetrahedral bonding pattern. This is also illustrated in the bottom panels, third row, of Fig. 3 (isovalue 0.006). In the ground state diamond structure of bulk silicon the sp<sup>3</sup> hybridisation allows the charge to accumulate in the four tetrahedral positions which are exactly the bond centers. In the case of a Si cluster, the non-tedrahedral arrangement of the nearest neighbors does not allow for this kind of optimal charge accumulation in the middle between two atoms. Instead the charge is distributed in some kind of irregular way in the interstitial region. If there is less charge, in between two atoms, the bond length is longer as a consequence of the Hellmann Feynman theorem. In addition one can find core atoms that have a much higher coordination than the bulk atoms.

**2. Surface to volume ratio.** Cutting surfaces costs energy because bonds are destroyed. Hence the surface area enters into many approximate formulas for the energy of nanoparticles. For the small cluster sizes we are considering, the definition of the surface area is somewhat ambiguous. We will adopt in this study a widely used approach of calculating surface areas in the context of solvation,<sup>76,77</sup> namely the soft-sphere implicit solvation model together with its calibration for an aqueous environment.<sup>78,79</sup> The particular choice of solvent is irrelevant for our purposes. The dielectric cavity is based on analytic smooth spheres centered on each atom, and it is fully continuous from the vacuum-like inner regions to the external bulk solvent.

[Fig. 4](../assets/figure/figure-4.jpg)

**Fig. 4** Correlation between the Kohn–Sham energy _E_<sub>KS</sub> of isomers and the surface to volume ratio of their soft-sphere cavity. Each box belongs to a particular cluster family. _E_<sub>KS</sub><sup>0</sup> is the KS energy of the global minimum. The color scale for data dots is based on the average bond distance (Å). The red dot represents the global minimum for each PES.

For each isomer we computed the surface and volume of the associated soft-sphere cavity. Fig. 4 shows the correlation between the Kohn–Sham energy $E_{KS}$ of the isomers and their surface to the volume ratio of their associated soft-sphere cavity. The plots show a high degree of correlation for all metallic clusters. In most cases the correlation is linear and low-lying isomers have a lower surface to volume ratio with respect to higher energy structures. The global minimum (red dots) coincides in general with the geometrical arrangement that minimizes this descriptor. Since the volume to surface ratio is strongly size dependent one can of course use this descriptor only for comparing clusters with the same number of atoms, where one can expect the volumes to be nearly constant.

So for a given number of atoms, there is a strong tendency to adopt compact shapes, but forming a nearly spherical cluster is not possible for any number of atoms as can be seen from the atomic arrangements shown in Fig. 1. The ground states show in general significant deviations from a perfect spherical shape. The icosahedron made out of 13 atoms (12 atoms from the 12 corners of the icoshedron and 1 central atom) is an exceptional case where one can form a quasi spherical shape. But with 15 spheres it is for instance not possible to obtain an approximately spherical shape by close packing spherical atoms of nearly identical size. The ground states of Na<sub>15</sub> and Mg<sub>15</sub> are consequently non-spherical.

The non-metallic clusters Ge<sub>15</sub>, Si<sub>10</sub>, Si<sub>15</sub> and Si<sub>20</sub> show hardly any correlation between the energy and the surface to volume ratio. The strong directional bonding prevents the cluster from adopting a nearly spherical shape.

**3. Shape factor.** In addition to the sphere, oblate and prolate ellipsoids can also have a low surface to volume ratio. The eigenvalues of the inertia tensor of the cluster can describe these shapes. Denoting the eigenvalues in increasing order by $\lambda_1 \le \lambda_2 \le \lambda_3$, we can define a shape factor $S$ as

$$S = \lambda_2/\lambda_3 - \lambda_1/\lambda_2 \qquad (3)$$

The length of the structure along the eigenvectors of the inertia tensor, called the principal axes of inertia, is given by the reciprocal square root of the eigenvalues. For a strongly oblate structure, which has two long axes and a short one, we have $\lambda_1 \approx \lambda_2 << \lambda_3$ and hence $S \approx -1$. For a strongly prolate structure, which has one long axis and two short ones, we have $\lambda_1 << \lambda_2 \approx \lambda_3$ and hence $S \approx 1$. So $S = 0$ indicates a spherical shape whereas positive values of $S$ indicate a prolate shape and negative values an oblate shape as shown in Fig. 5. The shape factor is actually not only zero for a sphere but for all Platonic solids (tetrahedron, cube, octahedron, dodecahedron and icosahedron). Such shapes are however not present in our data set, except the icosahedron which is indeed quite spherical.

[Fig. 5](../assets/figure/figure-5.jpg)

Fig. 5 An oblate (left) and prolate (right) shape. Figure taken from: https://en.wikipedia.org/wiki/Spheroid.

Fig. 6 shows the correlation between the Kohn–Sham energy $E_{\mathrm{KS}}$ of a given cluster local minimum and its shape factor $S$ defined by eqn (3). Values of the shape factor for all global minima are reported in Table 1. The preference for spherical shapes can be clearly seen for metallic clusters. Nevertheless many ground states, particularly with sizes in between the magic sizes of the jellium model, do not succeed to be close to spherical as can be deduced from the shape factors in Table 1. Higher energy metal cluster isomers typically adopt a prolate shape. While we limit our investigation to small clusters, a very similar behaviour based on geometrical shell completion was observed for a Na cluster with up to 147 atoms.<sup>6</sup> For geometrically magic sizes of 55 and 147 atoms the ground state is a spherical icosahedron. For the sizes in between, disordered ground states were found that deviate significantly from a spherical shape. A non-spherical ground state was also reported for the Na<sub>34</sub> cluster.<sup>33</sup>

No clear trends can be seen for the non-metalic clusters. For the Si<sub>20</sub> which has a prolate ground state, the energy rises continuously when the shape becomes more spherical.

The principal axes of inertia are frequently aligned with the structure’s symmetry axes. If a rigid body has an axis of symmetry of order $m$, meaning it is invariant under rotations of 360°/$m$ about the given axis, this axis is a principal axis. When $m > 2$, the rigid body is a symmetrical top. If a rigid body has at least two symmetry axes that are not parallel or perpendicular to each other, it is a spherical top.<sup>80</sup> The more symmetric the structure is, the more $S$ tends toward zero.

It is worth noticing that low-energy minima of clusters with a magic number of electrons (or near magic number, that is ±1 electrons with respect to a magic number) always have an almost zero shape factor. This holds, in particular, for the potential energy surface of the magic clusters Na<sub>8</sub>, Mg<sub>10</sub>, Mg<sub>10</sub><sup>+2</sup>, Mg<sub>11</sub><sup>+2</sup>, Al<sub>7</sub><sup>+1</sup>, Al<sub>13</sub><sup>−1</sup>, Al<sub>12</sub> Si, Al<sub>14</sub><sup>+2</sup>, and Si<sub>10</sub> (see Table 1). As a consequence, low-energy minima of magic clusters are highly symmetric and their arrangement tends toward a spherical top symmetry (see GM structures in Fig. 1). The spherical character of low lying isomers correlates with their higher coordination number ζ as shown in Fig. 2.

**4. Fingerprint distances to the global minimum.** Fig. 7 shows the correlation between the Kohn–Sham energy $E_{\mathrm{KS}}$ of the isomers relative to their ground state and their fingerprint distance<sup>81,82</sup> from the global minimum. A small fingerprint distance indicates a structural similarity whereas a large distance arises from important structural differences. We notice a remarkable linear correlation for all metallic clusters. This implies that whenever the structure becomes more similar to the ground state the energy will also go down. Hence there is a continuous driving force towards the ground state and the system will rapidly reach its ground state if the barriers along the way to the ground state are not too high compared to the thermal energy $k_{\mathrm{B}}T$. Even though we did not perform an exhaustive search for saddle points we found a few and they had very low barriers. For instance to cross from the ground state of Mg<sub>10</sub> to the first meta-stable structure, barriers of only about a mHa have to be crossed. These low barriers are related to the fact that saddle points in these metallic systems are frequently sandwiched in between two closely related minima structures, as shown in Fig. 8. A similar but more extensive investigation of gold clusters<sup>83</sup> has shown that most low energy structures can be transformed into other structures by crossing only very low barriers. Experimentally very low barriers have even been found for gold clusters of much larger size.<sup>84</sup> Because of this combination of steady driving force towards the global minimum and low barriers these metallic systems are expected to be structure seekers and the ground state should therefore be reachable with moderate annealing.

[Fig. 6](../assets/figure/figure-6.jpg)

Fig. 6 Correlation between the Kohn–Sham energy $E_{\mathrm{KS}}$ of isomers and their shape factor $S$ defined by eqn (3). Each box belongs to a particular cluster family. $E^{0}_{\mathrm{KS}}$ is the KS energy of the global minimum. The color scale for data dots is based on the average bond distance (Å). The red dot represents the global minimum for each PES.

[Fig. 7](../assets/figure/figure-7.jpg)

Fig. 7 Correlation between the Kohn–Sham energy $E_{\mathrm{KS}}$ of isomers and their fingerprint distance from the global minimum. Each box belongs to a particular cluster family. $E^{\mathrm{KS}}_{0}$ is the KS energy of the global minimum. The color scale for data dots is based on the average bond distance (Å). The red dot represents the global minimum for each PES.

[Fig. 8](../assets/figure/figure-8.jpg)

Fig. 8 The red spheres show the saddle point structure of Mg<sub>10</sub> that connects the ground state (blue spheres) with the first meta-stable structure (green spheres). To make the close similarity between these three structures visible, the radius had to be chosen much smaller than the standard covalent radius.

Only a weak correlation between the energy and fingerprint distance can be seen for the non-metallic clusters. Extensive annealing might be required experimentally to find the ground state and in some cases it might actually not be reachable.<sup>85</sup>

### B. Electronic properties

In this section we will investigate which electronic properties lead to low energy cluster structures. The electronic system will be characterized in terms of the density of states, the matching of the KS DFT eigenvalue degeneracies with the number of valence electrons, the gap between the highest occupied molecular orbital (Homo) and lowest unoccupied molecular orbital (Lumo) and the chemical hardness.

**1. Symmetry and electronic shells.** If a cluster belongs to a point group $G$ because of certain symmetries, the Kohn–Sham Hamiltonian $\mathcal{H}$ commutes with the symmetry operators $\hat{R}$ of $G$ if the self-consistent charge density has the same symmetry as the arrangement of the atoms in the cluster:

$$\forall \hat{R} \in G \rightarrow [\hat{R}, \mathcal{H}] = 0 \qquad (4)$$

Consequently the Kohn–Sham orbitals are eigenfunctions of both $\hat{R}$ and $\mathcal{H}$, and the eigenfunctions, that can be mapped onto each other by a symmetry operation, are degenerate. Filling an entire set of degenerate orbitals with the same number of possibly fractional electrons results in a charge density with the same symmetry as the cluster. Higher symmetries lead on average to higher degeneracies.

Table 1 gathers various structural and electronic properties of all global minima. Clusters that have a number of valence electrons that would classify the cluster size as magic in the jellium model are highlighted in bold in Table 1. However, as can be seen from the shape factors in Table 1, the shape of most of these clusters is quite non-spherical and the jellium model is not expected to be applicable. The failure of the jellium model can be seen from the fact that either the ideal shell ordering (1s, 1p, 1d, 2s, 1f, 2p) is reversed and/or some of these levels are split due to the symmetry breaking. These two effects have been studied in detail for Al clusters<sup>34,86</sup> and we have also found them in many of our clusters as can be seen from their DoS (Fig. 1). Nevertheless, in virtually all cases completely filled shells stabilize the ground state of the clusters.

[Fig. 9](../assets/figure/figure-9.jpg)

Fig. 9 The structure of the icosahedral GM of Al<sub>13</sub><sup>−1</sup> (red spheres) and the slightly distorted Al<sub>13</sub> ground state (blue spheres) with D<sub>3d</sub> symmetry. The radius of the spheres had to be taken much smaller than the covalent radius to see the small distortion.

The shells are frequently related to exact degeneracies arising from symmetry, but approximate degeneracies that arise from small symmetry reducing Jahn–Teller distortions, are even more important. We considered KS eigenvalues to have an approximate degeneracy if they differ by less then 10<sup>−2</sup> Ha. The Al<sub>13</sub><sup>−1</sup> cluster has for instance a high I<sub>h</sub> symmetry. Removing one electron leads to a small relaxation (see Fig. 9) that reduces the symmetry to D<sub>3d</sub>. The exact 3 and 4-fold degeneracies that exist in the I<sub>h</sub> group become approximate degeneracies (see Table 1) during the relaxation. The same effect can be seen in the non-metallic Si<sub>15</sub> cluster. Removing one electron reduces the symmetry from C<sub>3v</sub> to C<sub>s</sub> and the exact two fold degeneracy becomes an approximate degeneracy. Several other similar cases can be deduced from Table 1.

We call this process, which allows for the complete filling of shells formed by exact or approximate degeneracies, optimal matching, because the degeneracies of the occupied eigenvalues have to match the number of available electrons. The eigenvalue spectrum is of course determined by the structure of the cluster. So in an optimally matched cluster the atoms have to be able to find positions such that the resulting spectrum has shells that can be filled completely by the available number of electrons. We can see from Table 1 that it is not possible to find such an optimal matching for any number of atoms and electrons, using only the degeneracies related to symmetry. It is therefore not true that the ground state of a cluster is necessarily of high symmetry. We will later on discuss some clusters where the highest symmetry structure is only a low energy meta-stable structure but not the ground state. The systems for which such an optimal matching is possible are however in the majority of cases of higher symmetry, which results frequently from a moderate distortion of an even higher symmetry structure as discussed above. Approximate degeneracies are particularly important for small clusters with few electrons where a single approximate degeneracy can already have a large stabilizing effect.

[Fig. 10](../assets/figure/figure-10.jpg)

Fig. 10 The energy per atom of anionic Al clusters relative to Al<sub>13</sub><sup>−1</sup> together with the point group of the cluster. The trends are independent of the exchange correlation functional used (LDA or PBE).

[Fig. 11](../assets/figure/figure-11.jpg)

Fig. 11 Structures and density of states of the series of anionic Al clusters. The high stability of Al<sub>13</sub><sup>−1</sup> relative to other cluster sizes, shown in Fig. 10, clearly coincides with the high degeneracies of this cluster. See also Fig. S3 of the ESI† for a similar figure augmented by the data used to make the figure plus selected structural and electronic properties.

[Fig. 12](../assets/figure/figure-12.jpg)

Fig. 12 Lifting of the KS eigenvalue degeneracies by random atomic displacements away from the global minima. The effect for two different displacement amplitudes δ is shown, δ = 0.01 and 0.5 Å. See also Fig. S4 of the ESI† for a similar figure augmented by the data used to make the figure plus selected structural and electronic properties.

Table 2 Some meta-stable configurations with completely filled shells. The degeneracies of the KS orbitals are listed left to right going from the lowest to the highest occupied Kohn–Sham eigenvalue

[Table 2](../assets/table/table-2.csv)

| Cluster | Minimum | Number of electrons | Point group | Point group degeneracies | List of all KS DFT degeneracies |
| --- | --- | --- | --- | --- | --- |
| Mg10 | 1 (GM) | 20 | C3v | [1, 2] | [1, 1, 2, 1, 2, 2, 1] |
|  | 2 | 20 | C3v | [1, 2] | [1, 2, 1, 2, 1, 2, 1] |
|  | 3 | 20 | D4d | [1, 2] | [1, 1, 2, 1, 2, 2, 1] |
|  | 4 | 20 | C4v | [1, 2] | [1, 2, 1, 1, 2, 1, 1, 1] |
|  | 6 | 20 | Td | [1, 2, 3] | [1, 3, 1, 3, 2] |
|  | 12 | 20 | D2d | [1, 2] | [1, 1, 2, 1, 2, 1, 1, 1] |
| Al13^-1 | 1 (GM) | 40 | Ih | [1, 3, 4, 5] | [1, 3, 5, 1, 3, 3, 4] |
|  | 2 | 40 | C3v | [1, 2] | [1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1] |
|  | 4 | 40 | C3 | [1, 2] | [1, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 1] |
|  | 13 | 40 | C3v | [1, 2] | [1, 1, 2, 1, 2, 2, 1, 1, 1, 2, 3*, 1, 2] |
|  | 105 | 40 | C3v | [1, 2] | [1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1] |

When the optimal matching gives rise to a highly degenerate level, the cluster is particularly stable and is therefore expected to be found in large quantities in experimental spectra and to be thus a magic size. High degeneracy is in general related to high symmetry. The particularly low energy per atom of the ground state of optimally matched clusters is shown in Fig. 10 for the anionic Al clusters in the range between 10 and 22 atoms. This energy is on average of course decreasing as a function of cluster size and converging to the bulk value. Al<sub>13</sub><sup>−1</sup> has the highest symmetry (I<sub>h</sub>) and therefore by far the highest degree of degeneracy in the size range considered. As shown in Fig. 11, all the valence electrons are accommodated in seven shells arising from exact symmetries and in only five shells of near degeneracy. As a consequence it has the lowest energy per atom over a considerable range of cluster sizes.

Fig. 12 shows the density of states for various perturbed and unperturbed global minimum configurations. We consider the GM of Mg<sub>11</sub>, with a non-magic number of 22 valence electrons, and the GM of the clusters Al<sub>14</sub><sup>+2</sup> and Si<sub>10</sub>, both with the magic number of 40 valence electrons. These GM are particularly stable as shown by the large energetic distance of the first meta-stable configurations relative to the ground state (sharp increase of $E_{\mathrm{KS}}$ in the relative leftmost panels of Fig. 1) and their large HOMO–LUMO gap, reported in Table 1. For each system we extracted the electronic properties for the unperturbed (δ = 0.0 Å) structure as well as for structures where each atomic coordinate has been randomly displaced with an amplitude δ between 0.0 and 0.5 Å. Since we obtained the DoS plots by a convolution with a Gaussian of width 0.1 eV, the lifting of the degeneracies becomes visible only for random displacements with an amplitude of 0.5 Å or more. This random perturbation also has the side effect of reducing the HOMO–LUMO gap (see Fig. S4 of the ESI†). This analysis elucidates the process of structural adjustment towards the global minimum driven by an optimal matching condition for the nuclei configuration and valence electrons.

Among the meta-stable structures high symmetry structures with filled shells can also be found frequently as detailed in Table 2. Fig. 13 and 14 show that all the low energy structures of these metallic clusters try to be spherical and to form completely filled shells (see also Fig. S5 and S6 of the ESI† reporting additional structural and electronic data for the same structures). Moving from the eighth minimum to the GM of Al<sub>13</sub><sup>−1</sup> in Fig. 14, the formation of electronic shells and the adoption of a spherical arrangement is clearly visible. However the high symmetry structures with completely filled shells get rarer with increasing energy of the isomers. As shown in the histogram of Fig. 15, the abundance of high symmetry structures in all meta-stable configurations is much lower than in the ground state structures. In the ground state structures the C<sub>s</sub> and C<sub>3v</sub> symmetry dominate whereas the overwhelming majority of the meta-stable structures have no symmetry, *i.e.* belong to C<sub>1</sub>.

[Fig. 13](../assets/figure/figure-13.jpg)

Fig. 13 Structures and density of states of the first eight low-lying minima for the Mg<sub>10</sub> cluster. See also Fig. S5 of the ESI† for a similar figure augmented by the data used to make the figure plus selected structural and electronic properties.

[Fig. 14](../assets/figure/figure-14.jpg)

Fig. 14 Structures and density of states of the first eight low-lying minima for the Al<sub>13</sub><sup>−1</sup> cluster. See also Fig. S6 of the ESI† for a similar figure augmented by the data used to make the figure plus selected structural and electronic properties.

[Fig. 15](../assets/figure/figure-15.jpg)

Fig. 15 Histogram of the occurrences of all point groups in our cluster data set. Blue bins contain both ground states and meta-stable structures, and orange bins only ground state structures. Note the logarithmic scale along the *y*-axis. Point groups with a zero occurrence have been omitted.

The optimally matched clusters can also easily be recognized in the density of states plots in Fig. 1. In all these cases the density of states consists of a rather small number of narrow but high peaks arising from the degenerate shells and the Fermi level is in the middle of a large gap separating the fully occupied shells from the unoccupied shells. It does not matter whether the degeneracy comes from the spherically symmetric potential of the jellium model or whether it comes from another kind of high symmetry structure.

The energetically favorable high symmetry ground state structures always have several classes of equivalent atoms that see the same environment. In the Al<sub>13</sub><sup>−1</sup> cluster there are for instance two classes. The first comprises the 12 surface atoms of the icosahedron, and the second class consists only of the central atom. To obtain an overall low energy structure, the characteristic environments of the atoms defining the different classes must lead to low energy. When one transforms a high symmetry ground state into a meta-stable structure, at least one atom has to be moved. Since it was in a low energy position, the energy will typically increase strongly in such a move. In addition the corresponding moves of another atom in the same equivalence class will either give rise to an identical meta-stable structure or to a structure related by a symmetry operation. In both cases the increase in energy will be identical. Hence we can expect that we find only a relatively small number of structures in the funnel of a high symmetry ground state and that the energy gap between the ground state and the first meta-stable structure is relatively large. In a ground state with low symmetry all, or at least most atoms, have different environments, which are not all energetically optimal. Hence there are many possibilities to generate meta-stable structures and the energy increase will frequently be smaller since the starting point was already higher in energy. These expectations are confirmed by our data. The leftmost panel of each line in Fig. 1, corresponding to a cluster with a fixed number of atoms, shows the energy with respect to the ground state, $E_{\mathrm{KS}}–E^{0}_{\mathrm{KS}}$, for the energetically sorted meta-stable structures. Since $E_{\mathrm{KS}}–E^{0}_{\mathrm{KS}}$ increases rapidly for magic clusters, they have a deeper global minimum funnel containing a smaller number of meta-stable structures.

A more detailed description of a funnel can be obtained from a disconnectivity graph which also provides the height of the barriers that have to be crossed when hopping from one minimum of the potential energy surface to another one. The disconnectivity graphs in Fig. 16 show, in agreement with the $E_{\mathrm{KS}}$ curves in the panels at the left of Fig. 1, that Si<sub>10</sub> has the deepest funnel followed by the ionized Si<sub>10</sub> clusters. In agreement with Fig. 7, the disconnectivity graphs also show that only Si<sub>10</sub> and to a certain extent its ions are structure seekers whereas the other silicon clusters have a glassy energy landscape.

Since the spatial orbitals can always be filled with two electrons of opposite spin, a complete filling of the shells is only possible for clusters with an even number of electrons. For this reason all the magic clusters have an even number of electrons. If the neutral cluster has an odd number of electrons, the ionized cluster can sometimes be optimally matched. This is for instance the case in Al<sub>13</sub><sup>−1</sup> where the 40 valence electrons can completely fill all the shells of the jellium model. A complete filling of the shells is also observed for other clusters: the GM of Mg<sub>11</sub><sup>+2</sup> and Al<sub>7</sub><sup>+1</sup> with 20 electrons; the GM of Al<sub>12</sub> Si and Al<sub>14</sub><sup>+2</sup> with 40 electrons.

[Fig. 16](../assets/figure/figure-16.jpg)

Fig. 16 Disconnectivity graphs for selected silicon clusters.

For some well matched ground states, taking away or adding an electron can conserve up to slight distortions in the ground state such as in the Al<sub>13</sub> cluster shown in Fig. 1 or 9. However in many cases the ground state configuration of the ionized cluster does not coincide with the ground state of the neutral cluster.<sup>9</sup>

[Fig. 17](../assets/figure/figure-17.jpg)

Fig. 17 Correlation between the Kohn–Sham energy _E_<sub>KS</sub> of isomers and their HOMO–LUMO gaps. Each box belongs to a particular cluster family. _E_<sub>KS</sub><sup>0</sup> is the KS energy of the global minimum. The color scale for data dots is based on the average bond distance (Å). The red dot represents the global minimum for each PES.

[Fig. 18](../assets/figure/figure-18.jpg)

Fig. 18 Correlation between the Kohn–Sham energy _E_<sub>KS</sub> of isomers and their chemical hardness η. _E_<sub>KS</sub><sup>0</sup> is the KS energy of the global minimum. The color scale for data dots is based on the average bond distance (Å). The red dot represents the global minimum for each PES.

**2. HOMO–LUMO gap and chemical hardness.** A large HOMO–LUMO gap is generally considered as an indication of a high cluster stability. Our data in Fig. 17 show no significant correlation between the HOMO–LUMO gap and the total KS energy. Comparing however different systems one sees that the HOMO–LUMO gap is particularly large for the magic systems (see Table 1). For the energetically unfavorable clusters with an odd number of electrons the gaps are particularly small.

Closely related to the HOMO–LUMO gap is the chemical hardness η, defined as

$$\eta = \frac{1}{2}\left(\frac{\partial^2 E}{\partial m^2}\right)_n. \qquad (5)$$

Applying a three-point finite difference approximation, we can extract the chemical hardness from the vertical ionization energy E<sub>i</sub><sup>V</sup> and the vertical electron affinity E<sub>a</sub><sup>V</sup>

$$\eta = \frac{E_i^V - E_a^V}{2}. \qquad (6)$$

In a single particle scheme, the hardness is identical to the HOMO–LUMO gap. The vertical ionization energy E<sub>i</sub><sup>V</sup> is defined as the total energy difference between the (m − 1)-electron and the m-electron system with the cluster geometry kept fixed at the optimized m-electron configuration. Analogously, the vertical electron affinity E<sub>a</sub><sup>V</sup> is defined as the energy difference between the m-electron and the (m + 1)-electron system at the frozen m-electron configuration.

The maximum hardness principle<sup>87</sup> was originally proposed by Pearson. It states that ‘‘at equilibrium, chemical systems are as hard as possible’’. The chemical hardness quantifies the resistance to the changes in the number of electrons in the system, or to changes in the electronic density. A value of zero denotes maximum softness. For lithium clusters it was already shown that the magic size clusters are characterized by a particularly high hardness.<sup>88</sup>

Even though the correlation of the total energy with neither the ionization energy nor the electron affinity is good, the correlation with the hardness is very good. As shown in Fig. 18 there is a clear linear correlation between the Kohn–Sham energy _E_<sub>KS</sub> and the chemical hardness η. In most of the cases, the global minimum (red dot on each subgraph, data reported in Table 1) lies in the high η region of the PES. This is especially true for magic clusters or, in general, clusters with filled shells like the GM of Mg<sub>11</sub>, Si<sub>10</sub> and Si<sub>15</sub>.

### C. Selected clusters

To illustrate our stability criteria, we will in the following discuss in more detail some selected clusters.

In its ground state, the Mg<sub>11</sub> cluster can fill with its 22 electrons all the shells arising from a strongly non-spherical structure with D<sub>3h</sub> symmetry. So optimal matching can explain this ground state, but since the structure is less compact than Mg clusters made out of a different number of atoms, it is not expected to be a magic size.

The competition between adopting a spherical shape and the complete filling of shells can be well observed in the Na<sub>8</sub> and Mg<sub>10</sub> clusters. The T<sub>d</sub> structure of Na<sub>8</sub> (Fig. 19 or Fig. S7 of the ESI† reporting additional structural and electronic data for the same structures), which allows for complete filling of the two shells, is only the first meta-stable structure, while the ground state has three filled shells. For Mg<sub>10</sub> (Fig. 13) the highest symmetry structure is the tetrahedron which is however only the sixth meta-stable structure. The lower symmetry C<sub>3v</sub> structure is the ground state. In both cases the ground states are slightly more compact than the more symmetric meta-stable structures.

Fig. 20 illustrates nicely the role of optimal matching in Al<sub>13</sub>. Starting from the Al<sub>13</sub><sup>−1</sup> cluster which is an optimally matched cluster, we can either take away an electron while freezing the I<sub>h</sub> structure or keep the 40 electrons but transform the structure into the quite similar D<sub>3d</sub> ground state structure of the neutral Al<sub>13</sub>. In both cases degeneracies are lifted. In the first case the reason is that the incomplete filling of the electronic shells leads to Hartree and exchange correlation potentials of lower symmetry. In the second case the ionic potential arising from the nuclei is of lower symmetry. Both processes reduce the stability of the cluster. See also Fig. S8 of the ESI† for a similar figure augmented by the data used to make the figure.

[Fig. 19](../assets/figure/figure-19.jpg)

Fig. 19 Structures and density of states of the first two low-lying minima for the Na<sub>8</sub> cluster. The first meta-stable structure has higher degeneracies than the ground state, but is slightly more compact. See also Fig. S7 of the ESI† for a similar figure augmented by the data used to make the figure plus selected structural and electronic properties.

Optimal matching emerges also in the global minimum series of Al<sub>14</sub> with charge states q = −1, 0, 1, 2. Analysing how GM structures and DoS (Fig. 1), as well as the shape factor S (Table 1), change with a varying number of electrons, the optimal match of 40 electrons allows for a more stable spherical arrangement of the 14 atoms.

The Al<sub>12</sub>Si cluster should be extremely stable according to all criteria. It has a nearly perfect spherical shape, because of its high symmetry multiple degenerate shells, that are completely filled, as well as a very high HOMO—LUMO gap and hardness. According to general belief, it should therefore not be reactive. However it turns out that this cluster reacts easily with a second identical cluster. It is therefore not possible to build a cluster assembled material based on this cluster.<sup>89</sup> When two clusters are brought into contact during the assembly of such a material, they do not stay intact but form chemical bonds that destroy the 12 atom cage structure. A similar coalescence tendency was found for the Na<sub>8</sub> cluster.<sup>90</sup> For this magic cluster it was also shown that its spherical shape is destroyed upon deposition on a surface.

We analyzed the density of states of various clusters obtained from the global minimum of Al<sub>13</sub><sup>−1</sup>, that is the icosahedron, replacing its central atom with elements of the IV and V groups: Al<sub>13</sub><sup>−1</sup>, Al<sub>12</sub> C, Al<sub>12</sub> Si, Al<sub>12</sub> Ge, Al<sub>12</sub> Sn, Al<sub>12</sub>N<sup>+1</sup>, Al<sub>12</sub>P<sup>+1</sup>, Al<sub>12</sub>As<sup>+1</sup>, and Al<sub>12</sub>Sb<sup>+1</sup>. All of them hold the same magic number of valence electrons, that is 40, and, after their geometry optimization, the same icosahedron I<sub>h</sub> symmetry of the Al<sub>13</sub><sup>−1</sup> global minimum is displayed. The KS DFT eigenvalue degeneracies are identical for all icosahedrons, and their DoS maintains an identical shell structure with respect to the one of the Al<sub>13</sub><sup>−1</sup> global minimum. For some icosahedrons the order of appearance for the KS eigenvalue degeneracies or the distances between groups of degenerate eigenvalues are slightly modified. For example, comparing the KS eigenvalue degeneracies [1, 3, 5, 1, 3, 3, 4] of Al<sub>13</sub><sup>−1</sup> with the [1, 3, 1, 5, 3, 4, 3] ones of Al<sub>12</sub> C, we can notice an inversion of the third and fourth degeneracy levels. Similar differences appear when we compare other icosahedra. For all the Al<sub>12</sub> X icosahedra, with X being one of elements investigated, exchanging the X central atom with a surface atom breaks the cluster symmetry and, as a consequence, reduces the KS DFT eigenvalue degeneracies. The structure is still meta-stable but the energy is considerably higher. These pieces of evidence can only be accounted for by the optimal matching description, not by a structure-less jellium model.

[Fig. 20](../assets/figure/figure-20.jpg)

Fig. 20 Density of states of 40 (a) and 39 (b) valence electrons, distributed over a perfect icosahedron with point group I<sub>h</sub>. This structure is the GM of Al<sub>13</sub><sup>−1</sup> and has point group degeneracies [1, 3, 4, 5]. (c) The DoS of 40 electrons distributed over the slightly distorted icosahedron D<sub>3d</sub>, GM of Al<sub>13</sub>, which has point group degeneracies [1, 2]. See also Fig. S8 of the ESI† for a similar figure augmented by the data used to make the figure.

## IV. Conclusions

We have analysed the stability of a huge data set of isomer structures of representative clusters, containing the elements Na, Mg, Al, Si and Ge. The main criterion for stability is a perfect match between the degeneracies of the shells and the number of valence electrons that can fill these shells. These shells are frequently arising from approximate or accidental degeneracies. The atomic positions giving rise to a shell structure, that can accommodate the available number of electrons, can in general only be found by a structure search based on a global optimization algorithm. We call such a cluster whose shape gives rise to shells that can be completely filled by the number of available electrons an *optimally matched cluster*. If there are several optimally matched configurations the one which best satisfies other stability criteria will be lowest in energy. For our metallic structures we find a strong correlation between compactness and energetic stability. If the shape is nearly spherical the shell structure can be predicted by the jellium model if the electrons can be considered delocalized. Weak distortions away from a perfect spherical shape lead to splitting of the jellium shells and can change the energetic ordering of the shells. We have observed such small deviations from the ideal theoretical shell structures for most of our magic metallic clusters. Nevertheless the jellium model still correctly predicts magic sizes in these cases. If the cluster has a number of electrons that do not allow filling the shells of the jellium model completely, the model is of course not any more applicable. Our approach of optimally matched clusters is however still applicable. To obtain low energy, the cluster has to find an in general non-spherical shape that will give rise to shells that can completely be filled. So our approach can also explain the ground state structures of non-magic sizes.

For non-metallic clusters we could not find any tendency for spherical shapes. Hence jellium models are not applicable. As a matter of fact the stability of covalent clusters such as Si or Ge clusters was up to now nearly exclusively discussed in terms of certain structural motifs. Our approach of optimally matched clusters can however also be used in such cases and it can explain the in general strongly non-spherical ground state structures.

The bond lengths in metallic clusters are always considerably shorter than in the bulk metal. This is due to a flow of charge from the outside of the cluster to centers between neighboring atoms in the cluster. The effect is strongest for the low energy isomers.

In covalent clusters, the bond lengths are always longer than in the crystalline phase, since because of the directional bonding, it is not possible to accumulate charge exactly between each atom and all its nearest neighbors.

For all clusters the hardness and the energy difference between the first meta-stable structure and the ground state are good indicators for stability. In both cases large values indicate high stability. We have however no indications that a large hardness suppresses the chemical reactivity of clusters.

Our fingerprint-distance energy plots show that metallic clusters are structure seekers that can easily find their ground state by crossing only low barriers along a trajectory where they gain a significant amount of energy after each hop over a barrier. Experimentally they should therefore adopt their ground state with moderate annealing. This is however not true for covalent clusters. There the experimentally observed structure may not be the ground state but a structure that is kinetically more easily accessible.<sup>85</sup>

## Data availability

The data used to produce the results of this paper are openly available on the Materials Cloud Archive.<sup>55</sup>

## Conflicts of interest

There are no conflicts of interest to declare.

## Acknowledgements

We thank Bernd von Issendorff for the interesting discussions and for highlighting some literature. J.A.F. acknowledges financial support from the Swiss National Science Foundation (SNF) (project number 182877) and a joint SNF/DFG project (SPP 2363, SNF project number: 206936). This work was supported by a grant from the Swiss National Supercomputing Centre (CSCS) under project ID s963 and s1167.

## References

- 1 R. E. Leuchtner, A. C. Harms and A. W. Castleman, Thermal metal cluster anion reactions: Behavior of aluminum clusters with oxygen, J. Chem. Phys., 1989, 91, 2753.

- 2 P. Jena, S. N. Khanna and B. K. Rao, Physics and Chemistry of Finite Systems: From Clusters to Crystals, Springer, Netherlands, 1992.

- 3 A. Sanchez, S. Abbet, U. Heiz, W.-D. Schneider, H. Häkkinen, R. N. Barnett and U. Landman, When gold is not noble: Nanoscale gold catalysts, J. Phys. Chem. A, 1999, 103, 9573.

- 4 Z. Luo, A. W. Castleman and S. N. Khanna, Reactivity of metal clusters, Chem. Rev., 2016, 116, 14456.

- 5 K. Bao, S. Goedecker, K. Koga, F. Lançon and A. Neelov, Structure of large gold clusters obtained by global optimization using the minima hopping method, Phys. Rev. B: Condens. Matter Mater. Phys., 2009, 79, 041405.

- 6 I. Heidari, S. De, S. M. Ghazi, S. Goedecker and D. G. Kanhere, Growth and structural properties of mg-n (n = 10–56) clusters: Density functional theory study, J. Phys. Chem. A, 2011, 115, 12307.

- 7 S. M. Ghazi, S. De, D. G. Kanhere and S. Goedecker, Density functional investigations on structural and electronic properties of anionic and neutral sodium clusters na-n (n = 40–147): comparison with the experimental photoelectron spectra, J. Phys.: Condens. Matter, 2011, 23, 405303.

- 8 S. M. Ghazi, S. Zorriasatein and D. G. Kanhere, Building clusters atom-by-atom: From local order to global order, J. Phys. Chem. A, 2009, 113, 2659.

- 9 S. De, S. A. Ghasemi, A. Willand, L. Genovese, D. Kanhere and S. Goedecker, The effect of ionization on the global minima of small and medium sized silicon and magnesium clusters, J. Chem. Phys., 2011, 134, 124302.

- 10 E. C. Tyo and S. Vajda, Catalysis by clusters with precise numbers of atoms, Nat. Nanotechnol., 2015, 10, 577.

- 11 S. N. Khanna and P. Jena, Assembling crystals from clusters, Phys. Rev. Lett., 1992, 69, 1664.

- 12 S. A. Claridge, A. W. Castleman, S. N. Khanna, C. B. Murray, A. Sen and P. S. Weiss, Cluster-assembled materials, ACS Nano, 2009, 3, 244.

- 13 A. W. Castleman and S. N. Khanna, Clusters, superatoms, and building blocks of new materials, J. Phys. Chem. C, 2009, 113, 2664.

- 14 A. C. Reber and S. N. Khanna, Superatoms: Electronic and geometric effects on reactivity, Acc. Chem. Res., 2017, 50, 255.

- 15 S. N. Khanna and A. C. Reber, Intercalation without altercation, Nat. Chem., 2017, 9, 1151.

- 16 P. Jena and Q. Sun, Super atomic clusters: Design rules and potential for building blocks of materials, Chem. Rev., 2018, 118, 5755.

- 17 G. Fisicaro, A. La Magna, A. Alberti, E. Smecca, G. Mannino and I. Deretzis, Local order and rotational dynamics in mixed A-cation lead iodide perovskites, J. Phys. Chem. Lett., 2020, 11, 1068.

- 18 A. Pinkard, A. M. Champsaur and X. Roy, Molecular clusters: Nanoscale building blocks for solid-state materials, Acc. Chem. Res., 2018, 51, 919.

- 19 H. W. Kroto, J. R. Heath, S. C. OBrien, R. F. Curl and R. E. Smalley, C60: Buckminsterfullerene, Nature, 1985, 318, 162.

- 20 A. F. Hebard, M. J. Rosseinsky, R. C. Haddon, D. W. Murphy, S. H. Glarum, T. T. M. Palstra, A. P. Ramirez and A. R. Kortan, Superconductivity at 18 K in potassium-doped C60, Nature, 1991, 350, 600.

- 21 A. Y. Ganin, Y. Takabayashi, Y. Z. Khimyak, S. Margadonna, A. Tamai, M. J. Rosseinsky and K. Prassides, Bulk superconductivity at 38 K in a molecular system, Nat. Mater., 2008, 7, 367.

- 22 O. Echt, K. Sattler and E. Recknagel, Magic numbers for sphere packings: experimental verification in free xenon clusters, Phys. Rev. Lett., 1981, 47, 1121.

- 23 W. Miehle, O. Kandler, T. Leisner and O. Echt, Mass spectrometric evidence for icosahedral structure in large rare gas clusters: Ar, kr, xe, J. Chem. Phys., 1989, 91, 5940.

- 24 J. Pedersen, S. Bjørnholm, J. Borggreen, K. Hansen, T. Martin and H. Rasmussen, Observation of quantum supershells in clusters of sodium atoms, Nature, 1991, 353, 733.

- 25 W. D. Knight, K. Clemenger, W. A. de Heer, W. A. Saunders, M. Y. Chou and M. L. Cohen, Electronic shell structure and abundances of sodium clusters, Phys. Rev. Lett., 1984, 52, 2141.

- 26 K. Clemenger, Ellipsoidal shell structure in free-electron metal clusters, Phys. Rev. B: Condens. Matter Mater. Phys., 1985, 32, 1359.

- 27 W. A. de Heer, W. Knight, M. Chou and M. L. Cohen, Electronic shell structure and metal clusters, Academic Press, 1987, pp. 93–181.

- 28 T. Martin, T. Bergmann, H. Göhlich and T. Lange, Observation of electronic shells and shells of atoms in large na clusters, Chem. Phys. Lett., 1990, 172, 209.

- 29 C. Bartels, C. Hock, R. Kuhnen, M. Walter and B. V. Issendorff, Hybridization of angular-momentum eigenstates in nonspherical sodium clusters, Phys. Rev. A: At., Mol., Opt. Phys., 2013, 88, 043202.

- 30 A. Rytkönen, H. Häkkinen and M. Manninen, Melting and octupole deformation of na40, Phys. Rev. Lett., 1998, 80, 3940.

- 31 B. Montag, T. Hirschmann, J. Meyer, P.-G. Reinhard and M. Brack, Shape isomerism in sodium clusters with 10 ≤ z ≤ 44: Jellium model with quadrupole, octupole, and hexadecapole deformations, Phys. Rev. B: Condens. Matter Mater. Phys., 1995, 52, 4775.

- 32 M. Koskinen, P. Lipas and M. Manninen, Electron-gas clusters – the ultimate jellium model, Z. Phys. D: At., Mol. Clusters, 1995, 35, 285.

- 33 B. Huber, M. Moseler, O. Kostko and B. V.Issendorff, Structural evolution of the sodium cluster anions na<sub>20</sub><sup>−</sup>–na<sub>57</sub><sup>−</sup>, Phys. Rev. B: Condens. Matter Mater. Phys., 2009, 80, 235425.

- 34 L. Ma, B. v Issendorff and A. Aguado, Photoelectron spectroscopy of cold aluminum cluster anions: Comparison with density functional theory results, J. Chem. Phys., 2010, 132, 104303, DOI: 10.1063/1.3352445.

- 35 H. Häkkinen, M. Moseler, O. Kostko, N. Morgner, M. A. Hoffmann and B. V. Issendorff, Symmetry and electronic structure of noble-metal nanoparticles and the role of relativity, Phys. Rev. Lett., 2004, 93, 093401.

- 36 S. N. Khanna and P. Jena, Atomic clusters: Building blocks for a class of solids, Phys. Rev. B: Condens. Matter Mater. Phys., 1995, 51, 13705.

- 37 P. Jena, Beyond the periodic table of elements: The role of superatoms, J. Phys. Chem. Lett., 2013, 4, 1432, DOI: 10.1021/jz400156t.

- 38 P. Jena and Q. Sun, Superatoms: Principles, synthesis and applications, Wiley, 2022.

- 39 S. N. Khanna and A. W. Castleman, Quantum Phenomena in Clusters and Nanostructures, Springer, Berlin, Heidelberg, 2003.

- 40 D. E. Bergeron, A. W. Castleman, T. Morisato and S. N. Khanna, Formation of Al13I<sup>−</sup>: Evidence for the superhalogen character of Al13, Science, 2004, 304, 84.

- 41 G. Gutsev and A. Boldyrev, The way to systems with the highest possible electron affinity, Chem. Phys. Lett., 1984, 108, 250.

- 42 S. Goedecker, Minima hopping: An efficient eearch method for the global minimum of the potential energy surface of complex molecular systems, J. Chem. Phys., 2004, 120, 9911.

- 43 M. Sicher, S. Mohr and S. Goedecker, Efficient moves for global geometry optimization methods and their application to binary systems, J. Chem. Phys., 2011, 134, 044106.

- 44 S. Roy, S. Goedecker and V. Hellmann, Bell-E vans-P olanyi principle for molecular dynamics trajectories and its implications for global optimization, Phys. Rev. E: Stat., Nonlinear, Soft Matter Phys., 2008, 77, 056707.

- 45 B. Schaefer, S. Mohr, M. Amsler and S. Goedecker, Minima hopping guided path search: An efficient method for finding complex chemical reaction pathways, J. Chem. Phys., 2014, 140, 214102.

- 46 B. Schaefer, S. Alireza Ghasemi, S. Roy and S. Goedecker, Stabilized quasi-Newton optimization of noisy potential energy surfaces, J. Chem. Phys., 2015, 142, 034112.

- 47 L. Genovese, A. Neelov, S. Goedecker, T. Deutsch, S. A. Ghasemi, A. Willand, D. Caliste, O. Zilberberg, M. Rayson and A. Bergman, et al., Daubechies wavelets as a basis set for density functional pseudopotential calculations, J. Chem. Phys., 2008, 129, 014109.

- 48 L. E. Ratcliff, W. Dawson, G. Fisicaro, D. Caliste, S. Mohr, A. Degomme, B. Videau, V. Cristiglio, M. Stella, M. DAlessandro, S. Goedecker, T. Nakajima, T. Deutsch and L. Genovese, Flexibilities of wavelets as a computational basis set for large-scale electronic structure calculations, J. Chem. Phys., 2020, 152, 194110.

- 49 BigDFT software package, secondoftwo howpublished sanitize@url https://www.bigdft.org, accessed: 23-02-2022.

- 50 S. Goedecker, M. Teter and J. Hutter, Separable dual-space Gaussian pseudopotentials, Phys. Rev. B: Condens. Matter Mater. Phys., 1996, 54, 1703.

- 51 A. Willand, Y. O. Kvashnin, L. Genovese, A. Vázquez-Mayagoitia, A. K. Deb, A. Sadeghi, T. Deutsch and S. Goedecker, Norm-conserving pseudopotentials with chemical accuracy compared to all-electron calculations, J. Chem. Phys., 2013, 138, 104109.

- 52 J. P. Perdew, K. Burke and M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett., 1996, 77, 3865.

- 53 M. A. Marques, M. J. Oliveira and T. Burnus, Libxc: A library of exchange and correlation functionals for density functional theory, Comput. Phys. Comm., 2012, 183, 2272.

- 54 B. K. Rao, P. Jena and M. Manninen, Relationship between topological and magnetic order in small metal clusters, Phys. Rev. B: Condens. Matter Mater. Phys., 1985, 32, 477.

- 55 G. Fisicaro, B. Schaefer, J. A. Finkler and S. Goedecker, Principles of isomer stability in small clusters, Materials Cloud, 2023, DOI: 10.24435/materialscloud:46-nr.

- 56 A. J. Ceulemans, Group theory applied to chemistry, Springer, Dordrecht, 2013, p. 191.

- 57 The Materials Project, secondoftwo howpublished sanitize@url url https://materialsproject.org, accessed: 10-12-2021.

- 58 U. Röthlisberger and W. Andreoni, Structural and electronic properties of sodium microclusters (n = 2-20) at low and high temperatures: New insights from ab initio molecular dynamics studies, J. Chem. Phys., 1991, 94, 8129.

- 59 W. G. Sun, J. J. Wang, C. Lu, X. X. Xia, X. Y. Kuang and A. Hermann, Evolution of the structural and electronic properties of medium-sized sodium clusters: A honeycomblike Na20 cluster, Inorg. Chem., 2017, 56, 1241.

- 60 X. Xia, X. Kuang, C. Lu, Y. Jin, X. Xing, G. Merino and A. Hermann, Deciphering the structural evolution and electronic properties of magnesium clusters: An aromatic homonuclear metal Mg17 cluster, J. Phys. Chem. A, 2016, 120, 7947.

- 61 J. Jellinek and P. H. Acioli, Magnesium clusters: Structural and electronic properties and the size-induced nonmetal-tometal transition, J. Phys. Chem. A, 2003, 107, 1670.

- 62 A. Lyalin, I. A. Solovyov, A. V. Solovyov and W. Greiner, Evolution of the electronic and ionic structure of Mg clusters with increase in cluster size, Phys. Rev. A: At., Mol., Opt. Phys., 2003, 67, 063203.

- 63 I. Heidari, S. De, S. M. Ghazi, S. Goedecker and D. G. Kanhere, Growth and structural properties of Mgn (n = 10 − 56) clusters: Density functional theory study, J. Phys. Chem. A, 2011, 115, 12307.

- 64 B. K. Rao and P. Jena, Evolution of the electronic structure and properties of neutral and charged aluminum clusters: A comprehensive analysis, J. Chem. Phys., 1999, 111, 1890.

- 65 V. O. Kiohara, E. F. Carvalho, C. W. Paschoal, F. B. Machado and O. Roberto-Neto, DFT and CCSD(T) electronic properties and structures of aluminum clusters: Aln<sup>x</sup> (n = 1 − 9, x = 0,±1), Chem. Phys. Lett., 2013, 568–569, 42–48.

- 66 A. Aguado and J. M. López, Structures and stabilities of Aln<sup>+</sup>, Aln, and Aln<sup>−</sup> (n = 13-34) clusters, J. Chem. Phys., 2009, 130, 064704.

- 67 N. Drebov and R. Ahlrichs, Structures of Aln, its anions and cations up to n = 34: A theoretical investigation, J. Chem. Phys., 2010, 132, 164703.

- 68 F.-C. Chuang, C. Z. Wang and K. H. Ho, Structure of neutral aluminum clusters Aln (2 ≤ n ≤ 23): Genetic algorithm tight-binding calculations, Phys. Rev. B: Condens. Matter Mater. Phys., 2006, 73, 125431.

- 69 J. T. Lyon, P. Gruene, A. Fielicke, G. Meijer, E. Janssens, P. Claes and P. Lievens, Structures of silicon cluster cations in the gas phase, J. Am. Chem. Soc., 2009, 131, 1115.

- 70 K.-M. Ho, A. A. Shvartsburg, B. Pan, Z.-Y. Lu, C.-Z. Wang, J. G. Wacker, J. L. Fye and M. F. Jarrold, Structures of medium-sized silicon clusters, Nature, 1998, 392, 582.

- 71 M. Haertelt, J. T. Lyon, P. Claes, J. de Haeck, P. Lievens and A. Fielicke, Gas-phase structures of neutral silicon clusters, J. Chem. Phys., 2012, 136, 064301.

- 72 I. Rata, A. A. Shvartsburg, M. Horoi, T. Frauenheim, K. W. M. Siu and K. A. Jackson, Single-parent evolution algorithm and the optimization of si clusters, Phys. Rev. Lett., 2000, 85, 546.

- 73 K. A. Jackson, M. Horoi, I. Chaudhuri, T. Frauenheim and A. A. Shvartsburg, Unraveling the shape transformation in silicon clusters, Phys. Rev. Lett., 2004, 93, 013401.

- 74 W. Huang and L.-S. Wang, Probing the 2d to 3d structural transition in gold cluster anions using argon tagging, Phys. Rev. Lett., 2009, 102, 153401.

- 75 S. Gautam and A. D. Sarkar, A systematic investigation of acetylene activation and hydracyanation of the activated acetylene on aun (n = 3-10) clusters via density functional theory, Phys. Chem. Chem. Phys., 2016, 18, 13830.

- 76 G. Fisicaro, L. Genovese, O. Andreussi, N. Marzari and S. Goedecker, A generalized Poisson and Poisson-Boltzmann solver for electrostatic environments, J. Chem. Phys., 2016, 144, 014103.

- 77 O. Andreussi and G. Fisicaro, Continuum embeddings in condensed-matter simulations, Int. J. Quantum Chem., 2019, 119, e25725.

- 78 G. Fisicaro, L. Genovese, O. Andreussi, S. Mandal, N. N. Nair, N. Marzari and S. Goedecker, Soft-sphere continuum solvation in electronic-structure calculations, J. Chem. Theory Comput., 2017, 13, 3829.

- 79 G. Fisicaro, S. Filice, S. Scalese, G. Compagnini, R. Reitano, L. Genovese, S. Goedecker, I. Deretzis and A. L. Magna, J. Phys. Chem. C, 2020, 124, 2406–2419.

- 80 J. B. Marion and S. T. Thornton, Classical dynamics of particles and systems, Brooks/Cole Pub, 5th edn, 2004, ch. 11, p. 426.

- 81 S. De, B. Schaefer, A. Sadeghi, M. Sicher, D. G. Kanhere and S. Goedecker, Relation between the dynamics of glassy clusters and characteristic features of their energy landscape, Phys. Rev. Lett., 2014, 112, 083401.

- 82 A. Sadeghi, S. A. Ghasemi, B. Schaefer, S. Mohr, M. A. Lill and S. Goedecker, Metrics for measuring distances in configuration spaces, J. Chem. Phys., 2013, 139, 184118.

- 83 B. Schaefer, R. Pal, N. S. Khetrapal, M. Amsler, A. Sadeghi, V. Blum, X. C. Zeng, S. Goedecker and L.-S. Wang, Isomerism and Structural Fluxionality in the Au26 and Au26<sup>−</sup> Nanoclusters, ACS Nano, 2014, 8, 7413.

- 84 D. Foster, R. Ferrando and R. Palmer, Experimental determination of the energy difference between competing isomers of deposited, size-selected gold nanoclusters, Nat. Commun., 2018, 9, 1.

- 85 D. S. De, B. Schaefer, B. von Issendorff and S. Goedecker, Nonexistence of the decahedral Si20H20 cage: Levinthal’s paradox revisited, Phys. Rev. B, 2020, 101, 214303, DOI: 10.1103/PhysRevB.101.214303.

- 86 H.-P. Cheng, R. S. Berry and R. L. Whetten, Electronic structure and binding energies of aluminum clusters, Phys. Rev. B: Condens. Matter Mater. Phys., 1991, 43, 10647.

- 87 R. G. Pearson, The principle of maximum hardness, Acc. Chem. Res., 1993, 26, 250.

- 88 M. K. Harbola, Magic numbers for metallic clusters and the principle of maximum hardness, Proc. Natl. Acad. Sci. U. S. A., 1992, 89, 1036.

- 89 A. P. Seitsonen, M. J. Puska, M. Alatalo, R. M. Nieminen, V. Milman and M. C. Payne, Crystals from metallic clusters: A first-principles calculation, Phys. Rev. B: Condens. Matter Mater. Phys., 1993, 48, 1981.

- 90 H. Häkkinen and M. Manninen, How “magic” is a magic metal cluster?, Phys. Rev. Lett., 1996, 76, 1599.

## Conversion notes

- Inline notation for chemical sub/superscripts varies between HTML (<sub>/<sup>) and LaTeX ($...$) across sections; both are faithful transcriptions of the printed symbols.
- Floating Table 1 and several full-page figures (Figs 4, 6-8, 10-15, Table 2) were moved in reading order so that sentences interrupted by them read continuously; page provenance is preserved in the review evidence.
