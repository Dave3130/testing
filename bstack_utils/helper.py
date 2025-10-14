# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import collections
import datetime
import json
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
import sys
import logging
from math import ceil
from unittest import result
import urllib
from urllib.parse import urlparse
import copy
import zipfile
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import (bstack1l111l1l1l_opy_, bstack1111l11ll1_opy_, bstack111l1ll111_opy_,
                                    bstack11l11lll1l1_opy_, bstack11l1l11ll1l_opy_, bstack11l1l111l1l_opy_, bstack11l11lll11l_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1111l1l11l_opy_, bstack1l1llll1ll_opy_
from bstack_utils.proxy import bstack1l1l1l1111_opy_, bstack1l111ll1l_opy_
from bstack_utils.constants import *
from bstack_utils import bstack1ll1111ll_opy_
from bstack_utils.bstack1lll11l1l1_opy_ import bstack1l11l1l1ll_opy_
from browserstack_sdk._version import __version__
bstack111111ll_opy_ = Config.bstack1111lll1_opy_()
logger = bstack1ll1111ll_opy_.get_logger(__name__, bstack1ll1111ll_opy_.bstack1l1l111llll_opy_())
def bstack111l11lll1l_opy_(config):
    return config[bstack11l1l11_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᯃ")]
def bstack111l11ll111_opy_(config):
    return config[bstack11l1l11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᯄ")]
def bstack1111l11ll_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack1111ll1111l_opy_(obj):
    values = []
    bstack111l1111l11_opy_ = re.compile(bstack11l1l11_opy_ (u"ࡶࠧࡤࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢࡠࡩ࠱ࠤࠣᯅ"), re.I)
    for key in obj.keys():
        if bstack111l1111l11_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1111ll1l111_opy_(config):
    tags = []
    tags.extend(bstack1111ll1111l_opy_(os.environ))
    tags.extend(bstack1111ll1111l_opy_(config))
    return tags
def bstack111l1lllll1_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111l1llll11_opy_(bstack1111l1llll1_opy_):
    if not bstack1111l1llll1_opy_:
        return bstack11l1l11_opy_ (u"ࠬ࠭ᯆ")
    return bstack11l1l11_opy_ (u"ࠨࡻࡾࠢࠫࡿࢂ࠯ࠢᯇ").format(bstack1111l1llll1_opy_.name, bstack1111l1llll1_opy_.email)
def bstack1111ll11l1l_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111l1111111_opy_ = repo.common_dir
        info = {
            bstack11l1l11_opy_ (u"ࠢࡴࡪࡤࠦᯈ"): repo.head.commit.hexsha,
            bstack11l1l11_opy_ (u"ࠣࡵ࡫ࡳࡷࡺ࡟ࡴࡪࡤࠦᯉ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11l1l11_opy_ (u"ࠤࡥࡶࡦࡴࡣࡩࠤᯊ"): repo.active_branch.name,
            bstack11l1l11_opy_ (u"ࠥࡸࡦ࡭ࠢᯋ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11l1l11_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡸࡪࡸࠢᯌ"): bstack111l1llll11_opy_(repo.head.commit.committer),
            bstack11l1l11_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡹ࡫ࡲࡠࡦࡤࡸࡪࠨᯍ"): repo.head.commit.committed_datetime.isoformat(),
            bstack11l1l11_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࠨᯎ"): bstack111l1llll11_opy_(repo.head.commit.author),
            bstack11l1l11_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸ࡟ࡥࡣࡷࡩࠧᯏ"): repo.head.commit.authored_datetime.isoformat(),
            bstack11l1l11_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡠ࡯ࡨࡷࡸࡧࡧࡦࠤᯐ"): repo.head.commit.message,
            bstack11l1l11_opy_ (u"ࠤࡵࡳࡴࡺࠢᯑ"): repo.git.rev_parse(bstack11l1l11_opy_ (u"ࠥ࠱࠲ࡹࡨࡰࡹ࠰ࡸࡴࡶ࡬ࡦࡸࡨࡰࠧᯒ")),
            bstack11l1l11_opy_ (u"ࠦࡨࡵ࡭࡮ࡱࡱࡣ࡬࡯ࡴࡠࡦ࡬ࡶࠧᯓ"): bstack111l1111111_opy_,
            bstack11l1l11_opy_ (u"ࠧࡽ࡯ࡳ࡭ࡷࡶࡪ࡫࡟ࡨ࡫ࡷࡣࡩ࡯ࡲࠣᯔ"): subprocess.check_output([bstack11l1l11_opy_ (u"ࠨࡧࡪࡶࠥᯕ"), bstack11l1l11_opy_ (u"ࠢࡳࡧࡹ࠱ࡵࡧࡲࡴࡧࠥᯖ"), bstack11l1l11_opy_ (u"ࠣ࠯࠰࡫࡮ࡺ࠭ࡤࡱࡰࡱࡴࡴ࠭ࡥ࡫ࡵࠦᯗ")]).strip().decode(
                bstack11l1l11_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᯘ")),
            bstack11l1l11_opy_ (u"ࠥࡰࡦࡹࡴࡠࡶࡤ࡫ࠧᯙ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11l1l11_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡷࡤࡹࡩ࡯ࡥࡨࡣࡱࡧࡳࡵࡡࡷࡥ࡬ࠨᯚ"): repo.git.rev_list(
                bstack11l1l11_opy_ (u"ࠧࢁࡽ࠯࠰ࡾࢁࠧᯛ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack111ll1111ll_opy_ = []
        for remote in remotes:
            bstack111l1ll1111_opy_ = {
                bstack11l1l11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᯜ"): remote.name,
                bstack11l1l11_opy_ (u"ࠢࡶࡴ࡯ࠦᯝ"): remote.url,
            }
            bstack111ll1111ll_opy_.append(bstack111l1ll1111_opy_)
        bstack111l11l1l11_opy_ = {
            bstack11l1l11_opy_ (u"ࠣࡰࡤࡱࡪࠨᯞ"): bstack11l1l11_opy_ (u"ࠤࡪ࡭ࡹࠨᯟ"),
            **info,
            bstack11l1l11_opy_ (u"ࠥࡶࡪࡳ࡯ࡵࡧࡶࠦᯠ"): bstack111ll1111ll_opy_
        }
        bstack111l11l1l11_opy_ = bstack1111ll11ll1_opy_(bstack111l11l1l11_opy_)
        return bstack111l11l1l11_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11l1l11_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡴࡶࡵ࡭ࡣࡷ࡭ࡳ࡭ࠠࡈ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢᯡ").format(err))
        return {}
def bstack11lll1111ll_opy_(bstack1111llll11l_opy_=None):
    bstack11l1l11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡍࡥࡵࠢࡪ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡵࡳࡩࡨ࡯ࡦࡪࡥࡤࡰࡱࡿࠠࡧࡱࡵࡱࡦࡺࡴࡦࡦࠣࡪࡴࡸࠠࡂࡋࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦࡵࡴࡧࠣࡧࡦࡹࡥࡴࠢࡩࡳࡷࠦࡥࡢࡥ࡫ࠤ࡫ࡵ࡬ࡥࡧࡵࠤ࡮ࡴࠠࡵࡪࡨࠤࡱ࡯ࡳࡵ࠰ࠍࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡧࡱ࡯ࡨࡪࡸࡳࠡࠪ࡯࡭ࡸࡺࠬࠡࡱࡳࡸ࡮ࡵ࡮ࡢ࡮ࠬ࠾ࠥࡒࡩࡴࡶࠣࡳ࡫ࠦࡦࡰ࡮ࡧࡩࡷࠦࡰࡢࡶ࡫ࡷࠥࡺ࡯ࠡࡧࡻࡸࡷࡧࡣࡵࠢࡪ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡨࡵࡳࡲ࠴ࠠࡅࡧࡩࡥࡺࡲࡴࡴࠢࡷࡳࠥࡡ࡯ࡴ࠰ࡪࡩࡹࡩࡷࡥࠪࠬࡡ࠳ࠐࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࡬ࡪࡵࡷ࠾ࠥࡒࡩࡴࡶࠣࡳ࡫ࠦࡤࡪࡥࡷࡷ࠱ࠦࡥࡢࡥ࡫ࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮ࡴࡧࠡࡩ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡧࡱࡵࠤࡦࠦࡦࡰ࡮ࡧࡩࡷ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᯢ")
    if bstack1111llll11l_opy_ == None: # bstack111l1l11111_opy_ for bstack11lll11l1l1_opy_-repo
        bstack1111llll11l_opy_ = [os.getcwd()]
    results = []
    for folder in bstack1111llll11l_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack11l1l11_opy_ (u"ࠨࡰࡳࡋࡧࠦᯣ"): bstack11l1l11_opy_ (u"ࠢࠣᯤ"),
                bstack11l1l11_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢᯥ"): [],
                bstack11l1l11_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡵ᯦ࠥ"): [],
                bstack11l1l11_opy_ (u"ࠥࡴࡷࡊࡡࡵࡧࠥᯧ"): bstack11l1l11_opy_ (u"ࠦࠧᯨ"),
                bstack11l1l11_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡒ࡫ࡳࡴࡣࡪࡩࡸࠨᯩ"): [],
                bstack11l1l11_opy_ (u"ࠨࡰࡳࡖ࡬ࡸࡱ࡫ࠢᯪ"): bstack11l1l11_opy_ (u"ࠢࠣᯫ"),
                bstack11l1l11_opy_ (u"ࠣࡲࡵࡈࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠣᯬ"): bstack11l1l11_opy_ (u"ࠤࠥᯭ"),
                bstack11l1l11_opy_ (u"ࠥࡴࡷࡘࡡࡸࡆ࡬ࡪ࡫ࠨᯮ"): bstack11l1l11_opy_ (u"ࠦࠧᯯ")
            }
            bstack111l11111l1_opy_ = repo.active_branch.name
            bstack111ll1111l1_opy_ = repo.head.commit
            result[bstack11l1l11_opy_ (u"ࠧࡶࡲࡊࡦࠥᯰ")] = bstack111ll1111l1_opy_.hexsha
            bstack1111llll111_opy_ = _111ll111l11_opy_(repo)
            logger.debug(bstack11l1l11_opy_ (u"ࠨࡂࡢࡵࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤ࡫ࡵࡲࠡࡥࡲࡱࡵࡧࡲࡪࡵࡲࡲ࠿ࠦࠢᯱ") + str(bstack1111llll111_opy_) + bstack11l1l11_opy_ (u"᯲ࠢࠣ"))
            if bstack1111llll111_opy_:
                try:
                    bstack1111l1l11l1_opy_ = repo.git.diff(bstack11l1l11_opy_ (u"ࠣ࠯࠰ࡲࡦࡳࡥ࠮ࡱࡱࡰࡾࠨ᯳"), bstack1llll1111_opy_ (u"ࠤࡾࡦࡦࡹࡥࡠࡤࡵࡥࡳࡩࡨࡾ࠰࠱࠲ࢀࡩࡵࡳࡴࡨࡲࡹࡥࡢࡳࡣࡱࡧ࡭ࢃࠢ᯴")).split(bstack11l1l11_opy_ (u"ࠪࡠࡳ࠭᯵"))
                    logger.debug(bstack11l1l11_opy_ (u"ࠦࡈ࡮ࡡ࡯ࡩࡨࡨࠥ࡬ࡩ࡭ࡧࡶࠤࡧ࡫ࡴࡸࡧࡨࡲࠥࢁࡢࡢࡵࡨࡣࡧࡸࡡ࡯ࡥ࡫ࢁࠥࡧ࡮ࡥࠢࡾࡧࡺࡸࡲࡦࡰࡷࡣࡧࡸࡡ࡯ࡥ࡫ࢁ࠿ࠦࠢ᯶") + str(bstack1111l1l11l1_opy_) + bstack11l1l11_opy_ (u"ࠧࠨ᯷"))
                    result[bstack11l1l11_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧ᯸")] = [f.strip() for f in bstack1111l1l11l1_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1llll1111_opy_ (u"ࠢࡼࡤࡤࡷࡪࡥࡢࡳࡣࡱࡧ࡭ࢃ࠮࠯ࡽࡦࡹࡷࡸࡥ࡯ࡶࡢࡦࡷࡧ࡮ࡤࡪࢀࠦ᯹")))
                except Exception:
                    logger.debug(bstack11l1l11_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡬࡫ࡴࠡࡥ࡫ࡥࡳ࡭ࡥࡥࠢࡩ࡭ࡱ࡫ࡳࠡࡨࡵࡳࡲࠦࡢࡳࡣࡱࡧ࡭ࠦࡣࡰ࡯ࡳࡥࡷ࡯ࡳࡰࡰ࠱ࠤࡋࡧ࡬࡭࡫ࡱ࡫ࠥࡨࡡࡤ࡭ࠣࡸࡴࠦࡲࡦࡥࡨࡲࡹࠦࡣࡰ࡯ࡰ࡭ࡹࡹ࠮ࠣ᯺"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack11l1l11_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣ᯻")] = _111l1l1l1l1_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack11l1l11_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤ᯼")] = _111l1l1l1l1_opy_(commits[:5])
            bstack111l1l1l111_opy_ = set()
            bstack1111l1l11ll_opy_ = []
            for commit in commits:
                logger.debug(bstack11l1l11_opy_ (u"ࠦࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡥࡲࡱࡲ࡯ࡴ࠻ࠢࠥ᯽") + str(commit.message) + bstack11l1l11_opy_ (u"ࠧࠨ᯾"))
                bstack111l11l1ll1_opy_ = commit.author.name if commit.author else bstack11l1l11_opy_ (u"ࠨࡕ࡯࡭ࡱࡳࡼࡴࠢ᯿")
                bstack111l1l1l111_opy_.add(bstack111l11l1ll1_opy_)
                bstack1111l1l11ll_opy_.append({
                    bstack11l1l11_opy_ (u"ࠢ࡮ࡧࡶࡷࡦ࡭ࡥࠣᰀ"): commit.message.strip(),
                    bstack11l1l11_opy_ (u"ࠣࡷࡶࡩࡷࠨᰁ"): bstack111l11l1ll1_opy_
                })
            result[bstack11l1l11_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡵࠥᰂ")] = list(bstack111l1l1l111_opy_)
            result[bstack11l1l11_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡐࡩࡸࡹࡡࡨࡧࡶࠦᰃ")] = bstack1111l1l11ll_opy_
            result[bstack11l1l11_opy_ (u"ࠦࡵࡸࡄࡢࡶࡨࠦᰄ")] = bstack111ll1111l1_opy_.committed_datetime.strftime(bstack11l1l11_opy_ (u"࡙ࠧࠫ࠮ࠧࡰ࠱ࠪࡪࠢᰅ"))
            if (not result[bstack11l1l11_opy_ (u"ࠨࡰࡳࡖ࡬ࡸࡱ࡫ࠢᰆ")] or result[bstack11l1l11_opy_ (u"ࠢࡱࡴࡗ࡭ࡹࡲࡥࠣᰇ")].strip() == bstack11l1l11_opy_ (u"ࠣࠤᰈ")) and bstack111ll1111l1_opy_.message:
                bstack111l111llll_opy_ = bstack111ll1111l1_opy_.message.strip().splitlines()
                result[bstack11l1l11_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥᰉ")] = bstack111l111llll_opy_[0] if bstack111l111llll_opy_ else bstack11l1l11_opy_ (u"ࠥࠦᰊ")
                if len(bstack111l111llll_opy_) > 2:
                    result[bstack11l1l11_opy_ (u"ࠦࡵࡸࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠦᰋ")] = bstack11l1l11_opy_ (u"ࠬࡢ࡮ࠨᰌ").join(bstack111l111llll_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack11l1l11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡯ࡱࡷ࡯ࡥࡹ࡯࡮ࡨࠢࡊ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡨࡲࡶࠥࡇࡉࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱࠤ࠭࡬࡯࡭ࡦࡨࡶ࠿ࠦࡻࡧࡱ࡯ࡨࡪࡸࡽࠪ࠼ࠣࠦᰍ") + str(err) + bstack11l1l11_opy_ (u"ࠢࠣᰎ"))
    filtered_results = [
        result
        for result in results
        if _1111l1l1lll_opy_(result)
    ]
    return filtered_results
def _1111l1l1lll_opy_(result):
    bstack11l1l11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡊࡨࡰࡵ࡫ࡲࠡࡶࡲࠤࡨ࡮ࡥࡤ࡭ࠣ࡭࡫ࠦࡡࠡࡩ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡳࡧࡶࡹࡱࡺࠠࡪࡵࠣࡺࡦࡲࡩࡥࠢࠫࡲࡴࡴ࠭ࡦ࡯ࡳࡸࡾࠦࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠥࡧ࡮ࡥࠢࡤࡹࡹ࡮࡯ࡳࡵࠬ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᰏ")
    return (
        isinstance(result.get(bstack11l1l11_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣᰐ"), None), list)
        and len(result[bstack11l1l11_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤᰑ")]) > 0
        and isinstance(result.get(bstack11l1l11_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡷࠧᰒ"), None), list)
        and len(result[bstack11l1l11_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡸࠨᰓ")]) > 0
    )
def _111ll111l11_opy_(repo):
    bstack11l1l11_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡔࡳࡻࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡷ࡬ࡪࠦࡢࡢࡵࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥ࡭ࡩࡷࡧࡱࠤࡷ࡫ࡰࡰࠢࡺ࡭ࡹ࡮࡯ࡶࡶࠣ࡬ࡦࡸࡤࡤࡱࡧࡩࡩࠦ࡮ࡢ࡯ࡨࡷࠥࡧ࡮ࡥࠢࡺࡳࡷࡱࠠࡸ࡫ࡷ࡬ࠥࡧ࡬࡭࡙ࠢࡇࡘࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡲࡴ࠰ࠍࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡪࡥࡧࡣࡸࡰࡹࠦࡢࡳࡣࡱࡧ࡭ࠦࡩࡧࠢࡳࡳࡸࡹࡩࡣ࡮ࡨ࠰ࠥ࡫࡬ࡴࡧࠣࡒࡴࡴࡥ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᰔ")
    try:
        try:
            origin = repo.remotes.origin
            bstack1111llll1l1_opy_ = origin.refs[bstack11l1l11_opy_ (u"ࠧࡉࡇࡄࡈࠬᰕ")]
            target = bstack1111llll1l1_opy_.reference.name
            if target.startswith(bstack11l1l11_opy_ (u"ࠨࡱࡵ࡭࡬࡯࡮࠰ࠩᰖ")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack11l1l11_opy_ (u"ࠩࡲࡶ࡮࡭ࡩ࡯࠱ࠪᰗ")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _111l1l1l1l1_opy_(commits):
    bstack11l1l11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡋࡪࡺࠠ࡭࡫ࡶࡸࠥࡵࡦࠡࡥ࡫ࡥࡳ࡭ࡥࡥࠢࡩ࡭ࡱ࡫ࡳࠡࡨࡵࡳࡲࠦࡡࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢࡦࡳࡲࡳࡩࡵࡵ࠱ࠎࠥࠦࠠࠡࠤࠥࠦᰘ")
    bstack1111l1l11l1_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack111l11l11l1_opy_ in diff:
                        if bstack111l11l11l1_opy_.a_path:
                            bstack1111l1l11l1_opy_.add(bstack111l11l11l1_opy_.a_path)
                        if bstack111l11l11l1_opy_.b_path:
                            bstack1111l1l11l1_opy_.add(bstack111l11l11l1_opy_.b_path)
    except Exception:
        pass
    return list(bstack1111l1l11l1_opy_)
def bstack1111ll11ll1_opy_(bstack111l11l1l11_opy_):
    bstack111l11lllll_opy_ = bstack1111ll1l1l1_opy_(bstack111l11l1l11_opy_)
    if bstack111l11lllll_opy_ and bstack111l11lllll_opy_ > bstack11l11lll1l1_opy_:
        bstack111ll111111_opy_ = bstack111l11lllll_opy_ - bstack11l11lll1l1_opy_
        bstack111l1111l1l_opy_ = bstack111l11llll1_opy_(bstack111l11l1l11_opy_[bstack11l1l11_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧᰙ")], bstack111ll111111_opy_)
        bstack111l11l1l11_opy_[bstack11l1l11_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡤࡳࡥࡴࡵࡤ࡫ࡪࠨᰚ")] = bstack111l1111l1l_opy_
        logger.info(bstack11l1l11_opy_ (u"ࠨࡔࡩࡧࠣࡧࡴࡳ࡭ࡪࡶࠣ࡬ࡦࡹࠠࡣࡧࡨࡲࠥࡺࡲࡶࡰࡦࡥࡹ࡫ࡤ࠯ࠢࡖ࡭ࡿ࡫ࠠࡰࡨࠣࡧࡴࡳ࡭ࡪࡶࠣࡥ࡫ࡺࡥࡳࠢࡷࡶࡺࡴࡣࡢࡶ࡬ࡳࡳࠦࡩࡴࠢࡾࢁࠥࡑࡂࠣᰛ")
                    .format(bstack1111ll1l1l1_opy_(bstack111l11l1l11_opy_) / 1024))
    return bstack111l11l1l11_opy_
def bstack1111ll1l1l1_opy_(json_data):
    try:
        if json_data:
            bstack111l11l111l_opy_ = json.dumps(json_data)
            bstack1111ll1l1ll_opy_ = sys.getsizeof(bstack111l11l111l_opy_)
            return bstack1111ll1l1ll_opy_
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠢࡔࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭ࠠࡸࡪ࡬ࡰࡪࠦࡣࡢ࡮ࡦࡹࡱࡧࡴࡪࡰࡪࠤࡸ࡯ࡺࡦࠢࡲࡪࠥࡐࡓࡐࡐࠣࡳࡧࡰࡥࡤࡶ࠽ࠤࢀࢃࠢᰜ").format(e))
    return -1
def bstack111l11llll1_opy_(field, bstack111l1l1ll1l_opy_):
    try:
        bstack1111l1l1l1l_opy_ = len(bytes(bstack11l1l11ll1l_opy_, bstack11l1l11_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᰝ")))
        bstack1111lll111l_opy_ = bytes(field, bstack11l1l11_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᰞ"))
        bstack1111lll11ll_opy_ = len(bstack1111lll111l_opy_)
        bstack1111lll11l1_opy_ = ceil(bstack1111lll11ll_opy_ - bstack111l1l1ll1l_opy_ - bstack1111l1l1l1l_opy_)
        if bstack1111lll11l1_opy_ > 0:
            bstack111l11l1l1l_opy_ = bstack1111lll111l_opy_[:bstack1111lll11l1_opy_].decode(bstack11l1l11_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᰟ"), errors=bstack11l1l11_opy_ (u"ࠫ࡮࡭࡮ࡰࡴࡨࠫᰠ")) + bstack11l1l11ll1l_opy_
            return bstack111l11l1l1l_opy_
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡸࡷࡻ࡮ࡤࡣࡷ࡭ࡳ࡭ࠠࡧ࡫ࡨࡰࡩ࠲ࠠ࡯ࡱࡷ࡬࡮ࡴࡧࠡࡹࡤࡷࠥࡺࡲࡶࡰࡦࡥࡹ࡫ࡤࠡࡪࡨࡶࡪࡀࠠࡼࡿࠥᰡ").format(e))
    return field
def bstack11l11l1111_opy_():
    env = os.environ
    if (bstack11l1l11_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡖࡔࡏࠦᰢ") in env and len(env[bstack11l1l11_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡗࡕࡐࠧᰣ")]) > 0) or (
            bstack11l1l11_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡋࡓࡒࡋࠢᰤ") in env and len(env[bstack11l1l11_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢࡌࡔࡓࡅࠣᰥ")]) > 0):
        return {
            bstack11l1l11_opy_ (u"ࠥࡲࡦࡳࡥࠣᰦ"): bstack11l1l11_opy_ (u"ࠦࡏ࡫࡮࡬࡫ࡱࡷࠧᰧ"),
            bstack11l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᰨ"): env.get(bstack11l1l11_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᰩ")),
            bstack11l1l11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᰪ"): env.get(bstack11l1l11_opy_ (u"ࠣࡌࡒࡆࡤࡔࡁࡎࡇࠥᰫ")),
            bstack11l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᰬ"): env.get(bstack11l1l11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᰭ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠦࡈࡏࠢᰮ")) == bstack11l1l11_opy_ (u"ࠧࡺࡲࡶࡧࠥᰯ") and bstack1lll1ll1l1_opy_(env.get(bstack11l1l11_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡉࡉࠣᰰ"))):
        return {
            bstack11l1l11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᰱ"): bstack11l1l11_opy_ (u"ࠣࡅ࡬ࡶࡨࡲࡥࡄࡋࠥᰲ"),
            bstack11l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᰳ"): env.get(bstack11l1l11_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᰴ")),
            bstack11l1l11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᰵ"): env.get(bstack11l1l11_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡐࡏࡃࠤᰶ")),
            bstack11l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶ᰷ࠧ"): env.get(bstack11l1l11_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࠥ᰸"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠣࡅࡌࠦ᰹")) == bstack11l1l11_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ᰺") and bstack1lll1ll1l1_opy_(env.get(bstack11l1l11_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࠥ᰻"))):
        return {
            bstack11l1l11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᰼"): bstack11l1l11_opy_ (u"࡚ࠧࡲࡢࡸ࡬ࡷࠥࡉࡉࠣ᰽"),
            bstack11l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᰾"): env.get(bstack11l1l11_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡃࡗࡌࡐࡉࡥࡗࡆࡄࡢ࡙ࡗࡒࠢ᰿")),
            bstack11l1l11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᱀"): env.get(bstack11l1l11_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦ᱁")),
            bstack11l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᱂"): env.get(bstack11l1l11_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥ᱃"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠧࡉࡉࠣ᱄")) == bstack11l1l11_opy_ (u"ࠨࡴࡳࡷࡨࠦ᱅") and env.get(bstack11l1l11_opy_ (u"ࠢࡄࡋࡢࡒࡆࡓࡅࠣ᱆")) == bstack11l1l11_opy_ (u"ࠣࡥࡲࡨࡪࡹࡨࡪࡲࠥ᱇"):
        return {
            bstack11l1l11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᱈"): bstack11l1l11_opy_ (u"ࠥࡇࡴࡪࡥࡴࡪ࡬ࡴࠧ᱉"),
            bstack11l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᱊"): None,
            bstack11l1l11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᱋"): None,
            bstack11l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᱌"): None
        }
    if env.get(bstack11l1l11_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡆࡗࡇࡎࡄࡊࠥᱍ")) and env.get(bstack11l1l11_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡈࡕࡍࡎࡋࡗࠦᱎ")):
        return {
            bstack11l1l11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᱏ"): bstack11l1l11_opy_ (u"ࠥࡆ࡮ࡺࡢࡶࡥ࡮ࡩࡹࠨ᱐"),
            bstack11l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᱑"): env.get(bstack11l1l11_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡉࡌࡘࡤࡎࡔࡕࡒࡢࡓࡗࡏࡇࡊࡐࠥ᱒")),
            bstack11l1l11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᱓"): None,
            bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᱔"): env.get(bstack11l1l11_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥ᱕"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠤࡆࡍࠧ᱖")) == bstack11l1l11_opy_ (u"ࠥࡸࡷࡻࡥࠣ᱗") and bstack1lll1ll1l1_opy_(env.get(bstack11l1l11_opy_ (u"ࠦࡉࡘࡏࡏࡇࠥ᱘"))):
        return {
            bstack11l1l11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᱙"): bstack11l1l11_opy_ (u"ࠨࡄࡳࡱࡱࡩࠧᱚ"),
            bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᱛ"): env.get(bstack11l1l11_opy_ (u"ࠣࡆࡕࡓࡓࡋ࡟ࡃࡗࡌࡐࡉࡥࡌࡊࡐࡎࠦᱜ")),
            bstack11l1l11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᱝ"): None,
            bstack11l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᱞ"): env.get(bstack11l1l11_opy_ (u"ࠦࡉࡘࡏࡏࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᱟ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠧࡉࡉࠣᱠ")) == bstack11l1l11_opy_ (u"ࠨࡴࡳࡷࡨࠦᱡ") and bstack1lll1ll1l1_opy_(env.get(bstack11l1l11_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࠥᱢ"))):
        return {
            bstack11l1l11_opy_ (u"ࠣࡰࡤࡱࡪࠨᱣ"): bstack11l1l11_opy_ (u"ࠤࡖࡩࡲࡧࡰࡩࡱࡵࡩࠧᱤ"),
            bstack11l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᱥ"): env.get(bstack11l1l11_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡐࡔࡊࡅࡓࡏ࡚ࡂࡖࡌࡓࡓࡥࡕࡓࡎࠥᱦ")),
            bstack11l1l11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᱧ"): env.get(bstack11l1l11_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᱨ")),
            bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᱩ"): env.get(bstack11l1l11_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡋࡇࠦᱪ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠤࡆࡍࠧᱫ")) == bstack11l1l11_opy_ (u"ࠥࡸࡷࡻࡥࠣᱬ") and bstack1lll1ll1l1_opy_(env.get(bstack11l1l11_opy_ (u"ࠦࡌࡏࡔࡍࡃࡅࡣࡈࡏࠢᱭ"))):
        return {
            bstack11l1l11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᱮ"): bstack11l1l11_opy_ (u"ࠨࡇࡪࡶࡏࡥࡧࠨᱯ"),
            bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᱰ"): env.get(bstack11l1l11_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡗࡕࡐࠧᱱ")),
            bstack11l1l11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᱲ"): env.get(bstack11l1l11_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᱳ")),
            bstack11l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᱴ"): env.get(bstack11l1l11_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡏࡄࠣᱵ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠨࡃࡊࠤᱶ")) == bstack11l1l11_opy_ (u"ࠢࡵࡴࡸࡩࠧᱷ") and bstack1lll1ll1l1_opy_(env.get(bstack11l1l11_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࠦᱸ"))):
        return {
            bstack11l1l11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᱹ"): bstack11l1l11_opy_ (u"ࠥࡆࡺ࡯࡬ࡥ࡭࡬ࡸࡪࠨᱺ"),
            bstack11l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᱻ"): env.get(bstack11l1l11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᱼ")),
            bstack11l1l11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᱽ"): env.get(bstack11l1l11_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡐࡆࡈࡅࡍࠤ᱾")) or env.get(bstack11l1l11_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡎࡂࡏࡈࠦ᱿")),
            bstack11l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲀ"): env.get(bstack11l1l11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᲁ"))
        }
    if bstack1lll1ll1l1_opy_(env.get(bstack11l1l11_opy_ (u"࡙ࠦࡌ࡟ࡃࡗࡌࡐࡉࠨᲂ"))):
        return {
            bstack11l1l11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲃ"): bstack11l1l11_opy_ (u"ࠨࡖࡪࡵࡸࡥࡱࠦࡓࡵࡷࡧ࡭ࡴࠦࡔࡦࡣࡰࠤࡘ࡫ࡲࡷ࡫ࡦࡩࡸࠨᲄ"),
            bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᲅ"): bstack11l1l11_opy_ (u"ࠣࡽࢀࡿࢂࠨᲆ").format(env.get(bstack11l1l11_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡆࡐࡗࡑࡈࡆ࡚ࡉࡐࡐࡖࡉࡗ࡜ࡅࡓࡗࡕࡍࠬᲇ")), env.get(bstack11l1l11_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡑࡔࡒࡎࡊࡉࡔࡊࡆࠪᲈ"))),
            bstack11l1l11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲉ"): env.get(bstack11l1l11_opy_ (u"࡙࡙ࠧࡔࡖࡈࡑࡤࡊࡅࡇࡋࡑࡍ࡙ࡏࡏࡏࡋࡇࠦᲊ")),
            bstack11l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᲋"): env.get(bstack11l1l11_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢ᲌"))
        }
    if bstack1lll1ll1l1_opy_(env.get(bstack11l1l11_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࠥ᲍"))):
        return {
            bstack11l1l11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᲎"): bstack11l1l11_opy_ (u"ࠥࡅࡵࡶࡶࡦࡻࡲࡶࠧ᲏"),
            bstack11l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᲐ"): bstack11l1l11_opy_ (u"ࠧࢁࡽ࠰ࡲࡵࡳ࡯࡫ࡣࡵ࠱ࡾࢁ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠦᲑ").format(env.get(bstack11l1l11_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡗࡕࡐࠬᲒ")), env.get(bstack11l1l11_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡄࡇࡈࡕࡕࡏࡖࡢࡒࡆࡓࡅࠨᲓ")), env.get(bstack11l1l11_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡔࡗࡕࡊࡆࡅࡗࡣࡘࡒࡕࡈࠩᲔ")), env.get(bstack11l1l11_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭Ვ"))),
            bstack11l1l11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᲖ"): env.get(bstack11l1l11_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᲗ")),
            bstack11l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᲘ"): env.get(bstack11l1l11_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᲙ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠢࡂ࡜ࡘࡖࡊࡥࡈࡕࡖࡓࡣ࡚࡙ࡅࡓࡡࡄࡋࡊࡔࡔࠣᲚ")) and env.get(bstack11l1l11_opy_ (u"ࠣࡖࡉࡣࡇ࡛ࡉࡍࡆࠥᲛ")):
        return {
            bstack11l1l11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᲜ"): bstack11l1l11_opy_ (u"ࠥࡅࡿࡻࡲࡦࠢࡆࡍࠧᲝ"),
            bstack11l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᲞ"): bstack11l1l11_opy_ (u"ࠧࢁࡽࡼࡿ࠲ࡣࡧࡻࡩ࡭ࡦ࠲ࡶࡪࡹࡵ࡭ࡶࡶࡃࡧࡻࡩ࡭ࡦࡌࡨࡂࢁࡽࠣᲟ").format(env.get(bstack11l1l11_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡊࡔ࡛ࡎࡅࡃࡗࡍࡔࡔࡓࡆࡔ࡙ࡉࡗ࡛ࡒࡊࠩᲠ")), env.get(bstack11l1l11_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡕࡘࡏࡋࡇࡆࡘࠬᲡ")), env.get(bstack11l1l11_opy_ (u"ࠨࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠨᲢ"))),
            bstack11l1l11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᲣ"): env.get(bstack11l1l11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠥᲤ")),
            bstack11l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᲥ"): env.get(bstack11l1l11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧᲦ"))
        }
    if any([env.get(bstack11l1l11_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᲧ")), env.get(bstack11l1l11_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡖࡊ࡙ࡏࡍࡘࡈࡈࡤ࡙ࡏࡖࡔࡆࡉࡤ࡜ࡅࡓࡕࡌࡓࡓࠨᲨ")), env.get(bstack11l1l11_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡘࡕࡕࡓࡅࡈࡣ࡛ࡋࡒࡔࡋࡒࡒࠧᲩ"))]):
        return {
            bstack11l1l11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᲪ"): bstack11l1l11_opy_ (u"ࠥࡅ࡜࡙ࠠࡄࡱࡧࡩࡇࡻࡩ࡭ࡦࠥᲫ"),
            bstack11l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᲬ"): env.get(bstack11l1l11_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡒࡘࡆࡑࡏࡃࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᲭ")),
            bstack11l1l11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᲮ"): env.get(bstack11l1l11_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᲯ")),
            bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᲰ"): env.get(bstack11l1l11_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢᲱ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡐࡸࡱࡧ࡫ࡲࠣᲲ")):
        return {
            bstack11l1l11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲳ"): bstack11l1l11_opy_ (u"ࠧࡈࡡ࡮ࡤࡲࡳࠧᲴ"),
            bstack11l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᲵ"): env.get(bstack11l1l11_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡘࡥࡴࡷ࡯ࡸࡸ࡛ࡲ࡭ࠤᲶ")),
            bstack11l1l11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲷ"): env.get(bstack11l1l11_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡶ࡬ࡴࡸࡴࡋࡱࡥࡒࡦࡳࡥࠣᲸ")),
            bstack11l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᲹ"): env.get(bstack11l1l11_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡧࡻࡩ࡭ࡦࡑࡹࡲࡨࡥࡳࠤᲺ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࠨ᲻")) or env.get(bstack11l1l11_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡎࡃࡌࡒࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡔࡖࡄࡖ࡙ࡋࡄࠣ᲼")):
        return {
            bstack11l1l11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲽ"): bstack11l1l11_opy_ (u"࡙ࠣࡨࡶࡨࡱࡥࡳࠤᲾ"),
            bstack11l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲿ"): env.get(bstack11l1l11_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢ᳀")),
            bstack11l1l11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳁"): bstack11l1l11_opy_ (u"ࠧࡓࡡࡪࡰࠣࡔ࡮ࡶࡥ࡭࡫ࡱࡩࠧ᳂") if env.get(bstack11l1l11_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡎࡃࡌࡒࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡔࡖࡄࡖ࡙ࡋࡄࠣ᳃")) else None,
            bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᳄"): env.get(bstack11l1l11_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡊࡍ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨ᳅"))
        }
    if any([env.get(bstack11l1l11_opy_ (u"ࠤࡊࡇࡕࡥࡐࡓࡑࡍࡉࡈ࡚ࠢ᳆")), env.get(bstack11l1l11_opy_ (u"ࠥࡋࡈࡒࡏࡖࡆࡢࡔࡗࡕࡊࡆࡅࡗࠦ᳇")), env.get(bstack11l1l11_opy_ (u"ࠦࡌࡕࡏࡈࡎࡈࡣࡈࡒࡏࡖࡆࡢࡔࡗࡕࡊࡆࡅࡗࠦ᳈"))]):
        return {
            bstack11l1l11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᳉"): bstack11l1l11_opy_ (u"ࠨࡇࡰࡱࡪࡰࡪࠦࡃ࡭ࡱࡸࡨࠧ᳊"),
            bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᳋"): None,
            bstack11l1l11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᳌"): env.get(bstack11l1l11_opy_ (u"ࠤࡓࡖࡔࡐࡅࡄࡖࡢࡍࡉࠨ᳍")),
            bstack11l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳎"): env.get(bstack11l1l11_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨ᳏"))
        }
    if env.get(bstack11l1l11_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࠣ᳐")):
        return {
            bstack11l1l11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᳑"): bstack11l1l11_opy_ (u"ࠢࡔࡪ࡬ࡴࡵࡧࡢ࡭ࡧࠥ᳒"),
            bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᳓"): env.get(bstack11l1l11_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌ᳔ࠣ")),
            bstack11l1l11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩ᳕ࠧ"): bstack11l1l11_opy_ (u"ࠦࡏࡵࡢࠡࠥࡾࢁ᳖ࠧ").format(env.get(bstack11l1l11_opy_ (u"࡙ࠬࡈࡊࡒࡓࡅࡇࡒࡅࡠࡌࡒࡆࡤࡏࡄࠨ᳗"))) if env.get(bstack11l1l11_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡍࡓࡇࡥࡉࡅࠤ᳘")) else None,
            bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᳙"): env.get(bstack11l1l11_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥ᳚"))
        }
    if bstack1lll1ll1l1_opy_(env.get(bstack11l1l11_opy_ (u"ࠤࡑࡉ࡙ࡒࡉࡇ࡛ࠥ᳛"))):
        return {
            bstack11l1l11_opy_ (u"ࠥࡲࡦࡳࡥ᳜ࠣ"): bstack11l1l11_opy_ (u"ࠦࡓ࡫ࡴ࡭࡫ࡩࡽ᳝ࠧ"),
            bstack11l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬᳞ࠣ"): env.get(bstack11l1l11_opy_ (u"ࠨࡄࡆࡒࡏࡓ࡞ࡥࡕࡓࡎ᳟ࠥ")),
            bstack11l1l11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᳠"): env.get(bstack11l1l11_opy_ (u"ࠣࡕࡌࡘࡊࡥࡎࡂࡏࡈࠦ᳡")),
            bstack11l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲ᳢ࠣ"): env.get(bstack11l1l11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈ᳣ࠧ"))
        }
    if bstack1lll1ll1l1_opy_(env.get(bstack11l1l11_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣࡆࡉࡔࡊࡑࡑࡗ᳤ࠧ"))):
        return {
            bstack11l1l11_opy_ (u"ࠧࡴࡡ࡮ࡧ᳥ࠥ"): bstack11l1l11_opy_ (u"ࠨࡇࡪࡶࡋࡹࡧࠦࡁࡤࡶ࡬ࡳࡳࡹ᳦ࠢ"),
            bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮᳧ࠥ"): bstack11l1l11_opy_ (u"ࠣࡽࢀ࠳ࢀࢃ࠯ࡢࡥࡷ࡭ࡴࡴࡳ࠰ࡴࡸࡲࡸ࠵ࡻࡾࠤ᳨").format(env.get(bstack11l1l11_opy_ (u"ࠩࡊࡍ࡙ࡎࡕࡃࡡࡖࡉࡗ࡜ࡅࡓࡡࡘࡖࡑ࠭ᳩ")), env.get(bstack11l1l11_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡖࡊࡖࡏࡔࡋࡗࡓࡗ࡟ࠧᳪ")), env.get(bstack11l1l11_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡗ࡛ࡎࡠࡋࡇࠫᳫ"))),
            bstack11l1l11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᳬ"): env.get(bstack11l1l11_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡗࡐࡔࡎࡊࡑࡕࡗ᳭ࠣ")),
            bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᳮ"): env.get(bstack11l1l11_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠࡔࡘࡒࡤࡏࡄࠣᳯ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠤࡆࡍࠧᳰ")) == bstack11l1l11_opy_ (u"ࠥࡸࡷࡻࡥࠣᳱ") and env.get(bstack11l1l11_opy_ (u"࡛ࠦࡋࡒࡄࡇࡏࠦᳲ")) == bstack11l1l11_opy_ (u"ࠧ࠷ࠢᳳ"):
        return {
            bstack11l1l11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᳴"): bstack11l1l11_opy_ (u"ࠢࡗࡧࡵࡧࡪࡲࠢᳵ"),
            bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᳶ"): bstack11l1l11_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࡾࢁࠧ᳷").format(env.get(bstack11l1l11_opy_ (u"࡚ࠪࡊࡘࡃࡆࡎࡢ࡙ࡗࡒࠧ᳸"))),
            bstack11l1l11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳹"): None,
            bstack11l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᳺ"): None,
        }
    if env.get(bstack11l1l11_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡘࡈࡖࡘࡏࡏࡏࠤ᳻")):
        return {
            bstack11l1l11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᳼"): bstack11l1l11_opy_ (u"ࠣࡖࡨࡥࡲࡩࡩࡵࡻࠥ᳽"),
            bstack11l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᳾"): None,
            bstack11l1l11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᳿"): env.get(bstack11l1l11_opy_ (u"࡙ࠦࡋࡁࡎࡅࡌࡘ࡞ࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡏࡃࡐࡉࠧᴀ")),
            bstack11l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴁ"): env.get(bstack11l1l11_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᴂ"))
        }
    if any([env.get(bstack11l1l11_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࠥᴃ")), env.get(bstack11l1l11_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࡣ࡚ࡘࡌࠣᴄ")), env.get(bstack11l1l11_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠢᴅ")), env.get(bstack11l1l11_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡔࡆࡃࡐࠦᴆ"))]):
        return {
            bstack11l1l11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᴇ"): bstack11l1l11_opy_ (u"ࠧࡉ࡯࡯ࡥࡲࡹࡷࡹࡥࠣᴈ"),
            bstack11l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᴉ"): None,
            bstack11l1l11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᴊ"): env.get(bstack11l1l11_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᴋ")) or None,
            bstack11l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᴌ"): env.get(bstack11l1l11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᴍ"), 0)
        }
    if env.get(bstack11l1l11_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᴎ")):
        return {
            bstack11l1l11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴏ"): bstack11l1l11_opy_ (u"ࠨࡇࡰࡅࡇࠦᴐ"),
            bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴑ"): None,
            bstack11l1l11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᴒ"): env.get(bstack11l1l11_opy_ (u"ࠤࡊࡓࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᴓ")),
            bstack11l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᴔ"): env.get(bstack11l1l11_opy_ (u"ࠦࡌࡕ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡆࡓ࡚ࡔࡔࡆࡔࠥᴕ"))
        }
    if env.get(bstack11l1l11_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᴖ")):
        return {
            bstack11l1l11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᴗ"): bstack11l1l11_opy_ (u"ࠢࡄࡱࡧࡩࡋࡸࡥࡴࡪࠥᴘ"),
            bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᴙ"): env.get(bstack11l1l11_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᴚ")),
            bstack11l1l11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴛ"): env.get(bstack11l1l11_opy_ (u"ࠦࡈࡌ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡑࡅࡒࡋࠢᴜ")),
            bstack11l1l11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴝ"): env.get(bstack11l1l11_opy_ (u"ࠨࡃࡇࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᴞ"))
        }
    return {bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴟ"): None}
def get_host_info():
    return {
        bstack11l1l11_opy_ (u"ࠣࡪࡲࡷࡹࡴࡡ࡮ࡧࠥᴠ"): platform.node(),
        bstack11l1l11_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦᴡ"): platform.system(),
        bstack11l1l11_opy_ (u"ࠥࡸࡾࡶࡥࠣᴢ"): platform.machine(),
        bstack11l1l11_opy_ (u"ࠦࡻ࡫ࡲࡴ࡫ࡲࡲࠧᴣ"): platform.version(),
        bstack11l1l11_opy_ (u"ࠧࡧࡲࡤࡪࠥᴤ"): platform.architecture()[0]
    }
def bstack11111lll1_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111l111l1ll_opy_():
    if bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧᴥ")):
        return bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᴦ")
    return bstack11l1l11_opy_ (u"ࠨࡷࡱ࡯ࡳࡵࡷ࡯ࡡࡪࡶ࡮ࡪࠧᴧ")
def bstack1111ll111l1_opy_(driver):
    info = {
        bstack11l1l11_opy_ (u"ࠩࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨᴨ"): driver.capabilities,
        bstack11l1l11_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠧᴩ"): driver.session_id,
        bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬᴪ"): driver.capabilities.get(bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪᴫ"), None),
        bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᴬ"): driver.capabilities.get(bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᴭ"), None),
        bstack11l1l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᴮ"): driver.capabilities.get(bstack11l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨᴯ"), None),
        bstack11l1l11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᴰ"):driver.capabilities.get(bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᴱ"), None),
    }
    if bstack111l111l1ll_opy_() == bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᴲ"):
        if bstack1ll1l1lll_opy_():
            info[bstack11l1l11_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧᴳ")] = bstack11l1l11_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᴴ")
        elif driver.capabilities.get(bstack11l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᴵ"), {}).get(bstack11l1l11_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ᴶ"), False):
            info[bstack11l1l11_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫᴷ")] = bstack11l1l11_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨᴸ")
        else:
            info[bstack11l1l11_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᴹ")] = bstack11l1l11_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨᴺ")
    return info
def bstack1ll1l1lll_opy_():
    if bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᴻ")):
        return True
    if bstack1lll1ll1l1_opy_(os.environ.get(bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩᴼ"), None)):
        return True
    return False
def bstack11lll1llll_opy_(bstack1111l1ll111_opy_, url, data, config):
    headers = config.get(bstack11l1l11_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪᴽ"), None)
    proxies = bstack1l1l1l1111_opy_(config, url)
    auth = config.get(bstack11l1l11_opy_ (u"ࠪࡥࡺࡺࡨࠨᴾ"), None)
    response = requests.request(
            bstack1111l1ll111_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack11lllll111_opy_(bstack1l1llll1l_opy_, size):
    bstack1111ll1ll1_opy_ = []
    while len(bstack1l1llll1l_opy_) > size:
        bstack1lll1ll111_opy_ = bstack1l1llll1l_opy_[:size]
        bstack1111ll1ll1_opy_.append(bstack1lll1ll111_opy_)
        bstack1l1llll1l_opy_ = bstack1l1llll1l_opy_[size:]
    bstack1111ll1ll1_opy_.append(bstack1l1llll1l_opy_)
    return bstack1111ll1ll1_opy_
def bstack1111lll1l11_opy_(message, bstack111l111l111_opy_=False):
    os.write(1, bytes(message, bstack11l1l11_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᴿ")))
    os.write(1, bytes(bstack11l1l11_opy_ (u"ࠬࡢ࡮ࠨᵀ"), bstack11l1l11_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᵁ")))
    if bstack111l111l111_opy_:
        with open(bstack11l1l11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠭ࡰ࠳࠴ࡽ࠲࠭ᵂ") + os.environ[bstack11l1l11_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧᵃ")] + bstack11l1l11_opy_ (u"ࠩ࠱ࡰࡴ࡭ࠧᵄ"), bstack11l1l11_opy_ (u"ࠪࡥࠬᵅ")) as f:
            f.write(message + bstack11l1l11_opy_ (u"ࠫࡡࡴࠧᵆ"))
def bstack1llll11llll_opy_():
    return os.environ[bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨᵇ")].lower() == bstack11l1l11_opy_ (u"࠭ࡴࡳࡷࡨࠫᵈ")
def bstack1ll1ll11_opy_():
    return bstack1ll1l111_opy_().replace(tzinfo=None).isoformat() + bstack11l1l11_opy_ (u"࡛ࠧࠩᵉ")
def bstack1111l1ll11l_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11l1l11_opy_ (u"ࠨ࡜ࠪᵊ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11l1l11_opy_ (u"ࠩ࡝ࠫᵋ")))).total_seconds() * 1000
def bstack111l1lll1ll_opy_(timestamp):
    return bstack111l1l11lll_opy_(timestamp).isoformat() + bstack11l1l11_opy_ (u"ࠪ࡞ࠬᵌ")
def bstack1111lll1l1l_opy_(bstack111l1llll1l_opy_):
    date_format = bstack11l1l11_opy_ (u"ࠫࠪ࡟ࠥ࡮ࠧࡧࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠴ࠥࡧࠩᵍ")
    bstack111l1lll1l1_opy_ = datetime.datetime.strptime(bstack111l1llll1l_opy_, date_format)
    return bstack111l1lll1l1_opy_.isoformat() + bstack11l1l11_opy_ (u"ࠬࡠࠧᵎ")
def bstack1111lllllll_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11l1l11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᵏ")
    else:
        return bstack11l1l11_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᵐ")
def bstack1lll1ll1l1_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11l1l11_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᵑ")
def bstack111l111ll1l_opy_(val):
    return val.__str__().lower() == bstack11l1l11_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨᵒ")
def error_handler(bstack111l1l111ll_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111l1l111ll_opy_ as e:
                print(bstack11l1l11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࢀࢃࠠ࠮ࡀࠣࡿࢂࡀࠠࡼࡿࠥᵓ").format(func.__name__, bstack111l1l111ll_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack111l1l11l11_opy_(bstack111l1ll1l11_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack111l1ll1l11_opy_(cls, *args, **kwargs)
            except bstack111l1l111ll_opy_ as e:
                print(bstack11l1l11_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࢁࡽࠡ࠯ࡁࠤࢀࢃ࠺ࠡࡽࢀࠦᵔ").format(bstack111l1ll1l11_opy_.__name__, bstack111l1l111ll_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack111l1l11l11_opy_
    else:
        return decorator
def bstack1l1l11l1ll_opy_(bstack111ll1ll_opy_):
    if os.getenv(bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨᵕ")) is not None:
        return bstack1lll1ll1l1_opy_(os.getenv(bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩᵖ")))
    if bstack11l1l11_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᵗ") in bstack111ll1ll_opy_ and bstack111l111ll1l_opy_(bstack111ll1ll_opy_[bstack11l1l11_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᵘ")]):
        return False
    if bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᵙ") in bstack111ll1ll_opy_ and bstack111l111ll1l_opy_(bstack111ll1ll_opy_[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᵚ")]):
        return False
    return True
def bstack11ll1ll11_opy_():
    try:
        from pytest_bdd import reporting
        bstack111l11ll11l_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡙ࡘࡋࡒࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠦᵛ"), None)
        return bstack111l11ll11l_opy_ is None or bstack111l11ll11l_opy_ == bstack11l1l11_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤᵜ")
    except Exception as e:
        return False
def bstack1ll111l1l1_opy_(hub_url, CONFIG):
    if bstack11lll11ll_opy_() <= version.parse(bstack11l1l11_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ᵝ")):
        if hub_url:
            return bstack11l1l11_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣᵞ") + hub_url + bstack11l1l11_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧᵟ")
        return bstack1111l11ll1_opy_
    if hub_url:
        return bstack11l1l11_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦᵠ") + hub_url + bstack11l1l11_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦᵡ")
    return bstack111l1ll111_opy_
def bstack111l11lll11_opy_():
    return isinstance(os.getenv(bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡑ࡛ࡇࡊࡐࠪᵢ")), str)
def bstack1ll1l111l_opy_(url):
    return urlparse(url).hostname
def bstack1l1ll11ll1_opy_(hostname):
    for bstack1l1l11111_opy_ in bstack1l111l1l1l_opy_:
        regex = re.compile(bstack1l1l11111_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll11l111l_opy_(bstack111l1l1ll11_opy_, file_name, logger):
    bstack1l1l1ll1l_opy_ = os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"ࠬࢄࠧᵣ")), bstack111l1l1ll11_opy_)
    try:
        if not os.path.exists(bstack1l1l1ll1l_opy_):
            os.makedirs(bstack1l1l1ll1l_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"࠭ࡾࠨᵤ")), bstack111l1l1ll11_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11l1l11_opy_ (u"ࠧࡸࠩᵥ")):
                pass
            with open(file_path, bstack11l1l11_opy_ (u"ࠣࡹ࠮ࠦᵦ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1111l1l11l_opy_.format(str(e)))
def bstack11ll111l1ll_opy_(file_name, key, value, logger):
    file_path = bstack11ll11l111l_opy_(bstack11l1l11_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᵧ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1111l111l1_opy_ = json.load(open(file_path, bstack11l1l11_opy_ (u"ࠪࡶࡧ࠭ᵨ")))
        else:
            bstack1111l111l1_opy_ = {}
        bstack1111l111l1_opy_[key] = value
        with open(file_path, bstack11l1l11_opy_ (u"ࠦࡼ࠱ࠢᵩ")) as outfile:
            json.dump(bstack1111l111l1_opy_, outfile)
def bstack11lll1l111_opy_(file_name, logger):
    file_path = bstack11ll11l111l_opy_(bstack11l1l11_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᵪ"), file_name, logger)
    bstack1111l111l1_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11l1l11_opy_ (u"࠭ࡲࠨᵫ")) as bstack111lll1l1_opy_:
            bstack1111l111l1_opy_ = json.load(bstack111lll1l1_opy_)
    return bstack1111l111l1_opy_
def bstack1l11llll1l_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡧࡩࡱ࡫ࡴࡪࡰࡪࠤ࡫࡯࡬ࡦ࠼ࠣࠫᵬ") + file_path + bstack11l1l11_opy_ (u"ࠨࠢࠪᵭ") + str(e))
def bstack11lll11ll_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11l1l11_opy_ (u"ࠤ࠿ࡒࡔ࡚ࡓࡆࡖࡁࠦᵮ")
def bstack11ll1lllll_opy_(config):
    if bstack11l1l11_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᵯ") in config:
        del (config[bstack11l1l11_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᵰ")])
        return False
    if bstack11lll11ll_opy_() < version.parse(bstack11l1l11_opy_ (u"ࠬ࠹࠮࠵࠰࠳ࠫᵱ")):
        return False
    if bstack11lll11ll_opy_() >= version.parse(bstack11l1l11_opy_ (u"࠭࠴࠯࠳࠱࠹ࠬᵲ")):
        return True
    if bstack11l1l11_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧᵳ") in config and config[bstack11l1l11_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨᵴ")] is False:
        return False
    else:
        return True
def bstack11111llll1_opy_(args_list, bstack111l1l1l11l_opy_):
    index = -1
    for value in bstack111l1l1l11l_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack1111l1lll1l_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack1111l1lll1l_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack11lll1l1_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack11lll1l1_opy_ = bstack11lll1l1_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack11l1l11_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᵵ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11l1l11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᵶ"), exception=exception)
    def bstack11111l111l_opy_(self):
        if self.result != bstack11l1l11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᵷ"):
            return None
        if isinstance(self.exception_type, str) and bstack11l1l11_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣᵸ") in self.exception_type:
            return bstack11l1l11_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢᵹ")
        return bstack11l1l11_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣᵺ")
    def bstack111l1llllll_opy_(self):
        if self.result != bstack11l1l11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᵻ"):
            return None
        if self.bstack11lll1l1_opy_:
            return self.bstack11lll1l1_opy_
        return bstack111l11l11ll_opy_(self.exception)
def bstack111l11l11ll_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111l1ll1lll_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack11lll111_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1ll1111l11_opy_(config, logger):
    try:
        import playwright
        bstack111l1111lll_opy_ = playwright.__file__
        bstack1111l1ll1l1_opy_ = os.path.split(bstack111l1111lll_opy_)
        bstack111l11l1111_opy_ = bstack1111l1ll1l1_opy_[0] + bstack11l1l11_opy_ (u"ࠩ࠲ࡨࡷ࡯ࡶࡦࡴ࠲ࡴࡦࡩ࡫ࡢࡩࡨ࠳ࡱ࡯ࡢ࠰ࡥ࡯࡭࠴ࡩ࡬ࡪ࠰࡭ࡷࠬᵼ")
        os.environ[bstack11l1l11_opy_ (u"ࠪࡋࡑࡕࡂࡂࡎࡢࡅࡌࡋࡎࡕࡡࡋࡘ࡙ࡖ࡟ࡑࡔࡒ࡜࡞࠭ᵽ")] = bstack1l111ll1l_opy_(config)
        with open(bstack111l11l1111_opy_, bstack11l1l11_opy_ (u"ࠫࡷ࠭ᵾ")) as f:
            file_content = f.read()
            bstack111l1l1l1ll_opy_ = bstack11l1l11_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠫᵿ")
            bstack111ll11111l_opy_ = file_content.find(bstack111l1l1l1ll_opy_)
            if bstack111ll11111l_opy_ == -1:
              process = subprocess.Popen(bstack11l1l11_opy_ (u"ࠨ࡮ࡱ࡯ࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠥᶀ"), shell=True, cwd=bstack1111l1ll1l1_opy_[0])
              process.wait()
              bstack111l1ll1ll1_opy_ = bstack11l1l11_opy_ (u"ࠧࠣࡷࡶࡩࠥࡹࡴࡳ࡫ࡦࡸࠧࡁࠧᶁ")
              bstack1111l1lllll_opy_ = bstack11l1l11_opy_ (u"ࠣࠤࠥࠤࡡࠨࡵࡴࡧࠣࡷࡹࡸࡩࡤࡶ࡟ࠦࡀࠦࡣࡰࡰࡶࡸࠥࢁࠠࡣࡱࡲࡸࡸࡺࡲࡢࡲࠣࢁࠥࡃࠠࡳࡧࡴࡹ࡮ࡸࡥࠩࠩࡪࡰࡴࡨࡡ࡭࠯ࡤ࡫ࡪࡴࡴࠨࠫ࠾ࠤ࡮࡬ࠠࠩࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡨࡲࡻ࠴ࡇࡍࡑࡅࡅࡑࡥࡁࡈࡇࡑࡘࡤࡎࡔࡕࡒࡢࡔࡗࡕࡘ࡚ࠫࠣࡦࡴࡵࡴࡴࡶࡵࡥࡵ࠮ࠩ࠼ࠢࠥࠦࠧᶂ")
              bstack111l111111l_opy_ = file_content.replace(bstack111l1ll1ll1_opy_, bstack1111l1lllll_opy_)
              with open(bstack111l11l1111_opy_, bstack11l1l11_opy_ (u"ࠩࡺࠫᶃ")) as f:
                f.write(bstack111l111111l_opy_)
    except Exception as e:
        logger.error(bstack1l1llll1ll_opy_.format(str(e)))
def bstack1111lll1l_opy_():
  try:
    bstack111l1l1111l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠪࡳࡵࡺࡩ࡮ࡣ࡯ࡣ࡭ࡻࡢࡠࡷࡵࡰ࠳ࡰࡳࡰࡰࠪᶄ"))
    bstack111l111lll1_opy_ = []
    if os.path.exists(bstack111l1l1111l_opy_):
      with open(bstack111l1l1111l_opy_) as f:
        bstack111l111lll1_opy_ = json.load(f)
      os.remove(bstack111l1l1111l_opy_)
    return bstack111l111lll1_opy_
  except:
    pass
  return []
def bstack11l1ll111_opy_(bstack111ll11lll_opy_):
  try:
    bstack111l111lll1_opy_ = []
    bstack111l1l1111l_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠴ࡪࡴࡱࡱࠫᶅ"))
    if os.path.exists(bstack111l1l1111l_opy_):
      with open(bstack111l1l1111l_opy_) as f:
        bstack111l111lll1_opy_ = json.load(f)
    bstack111l111lll1_opy_.append(bstack111ll11lll_opy_)
    with open(bstack111l1l1111l_opy_, bstack11l1l11_opy_ (u"ࠬࡽࠧᶆ")) as f:
        json.dump(bstack111l111lll1_opy_, f)
  except:
    pass
def bstack1ll111ll1l_opy_(logger, bstack1111llll1ll_opy_ = False):
  try:
    test_name = os.environ.get(bstack11l1l11_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩᶇ"), bstack11l1l11_opy_ (u"ࠧࠨᶈ"))
    if test_name == bstack11l1l11_opy_ (u"ࠨࠩᶉ"):
        test_name = threading.current_thread().__dict__.get(bstack11l1l11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡄࡧࡨࡤࡺࡥࡴࡶࡢࡲࡦࡳࡥࠨᶊ"), bstack11l1l11_opy_ (u"ࠪࠫᶋ"))
    bstack111l111l1l1_opy_ = bstack11l1l11_opy_ (u"ࠫ࠱ࠦࠧᶌ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack1111llll1ll_opy_:
        bstack11111l11l_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬᶍ"), bstack11l1l11_opy_ (u"࠭࠰ࠨᶎ"))
        bstack11ll11ll1_opy_ = {bstack11l1l11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᶏ"): test_name, bstack11l1l11_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᶐ"): bstack111l111l1l1_opy_, bstack11l1l11_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᶑ"): bstack11111l11l_opy_}
        bstack111l1ll1l1l_opy_ = []
        bstack1111ll1llll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡴࡵࡶ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩᶒ"))
        if os.path.exists(bstack1111ll1llll_opy_):
            with open(bstack1111ll1llll_opy_) as f:
                bstack111l1ll1l1l_opy_ = json.load(f)
        bstack111l1ll1l1l_opy_.append(bstack11ll11ll1_opy_)
        with open(bstack1111ll1llll_opy_, bstack11l1l11_opy_ (u"ࠫࡼ࠭ᶓ")) as f:
            json.dump(bstack111l1ll1l1l_opy_, f)
    else:
        bstack11ll11ll1_opy_ = {bstack11l1l11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᶔ"): test_name, bstack11l1l11_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᶕ"): bstack111l111l1l1_opy_, bstack11l1l11_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ᶖ"): str(multiprocessing.current_process().name)}
        if bstack11l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸࠬᶗ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack11ll11ll1_opy_)
  except Exception as e:
      logger.warn(bstack11l1l11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡵࡿࡴࡦࡵࡷࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢ࠼ࠣࡿࢂࠨᶘ").format(e))
def bstack11llllll11_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l1l11_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠥࡴ࡯ࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥࡨࡡࡴ࡫ࡦࠤ࡫࡯࡬ࡦࠢࡲࡴࡪࡸࡡࡵ࡫ࡲࡲࡸ࠭ᶙ"))
    try:
      bstack1111ll1lll1_opy_ = []
      bstack11ll11ll1_opy_ = {bstack11l1l11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᶚ"): test_name, bstack11l1l11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᶛ"): error_message, bstack11l1l11_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᶜ"): index}
      bstack1111ll111ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠧࡳࡱࡥࡳࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨᶝ"))
      if os.path.exists(bstack1111ll111ll_opy_):
          with open(bstack1111ll111ll_opy_) as f:
              bstack1111ll1lll1_opy_ = json.load(f)
      bstack1111ll1lll1_opy_.append(bstack11ll11ll1_opy_)
      with open(bstack1111ll111ll_opy_, bstack11l1l11_opy_ (u"ࠨࡹࠪᶞ")) as f:
          json.dump(bstack1111ll1lll1_opy_, f)
    except Exception as e:
      logger.warn(bstack11l1l11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡷࡵࡢࡰࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧᶟ").format(e))
    return
  bstack1111ll1lll1_opy_ = []
  bstack11ll11ll1_opy_ = {bstack11l1l11_opy_ (u"ࠪࡲࡦࡳࡥࠨᶠ"): test_name, bstack11l1l11_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᶡ"): error_message, bstack11l1l11_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᶢ"): index}
  bstack1111ll111ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"࠭ࡲࡰࡤࡲࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧᶣ"))
  lock_file = bstack1111ll111ll_opy_ + bstack11l1l11_opy_ (u"ࠧ࠯࡮ࡲࡧࡰ࠭ᶤ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1111ll111ll_opy_):
          with open(bstack1111ll111ll_opy_, bstack11l1l11_opy_ (u"ࠨࡴࠪᶥ")) as f:
              content = f.read().strip()
              if content:
                  bstack1111ll1lll1_opy_ = json.load(open(bstack1111ll111ll_opy_))
      bstack1111ll1lll1_opy_.append(bstack11ll11ll1_opy_)
      with open(bstack1111ll111ll_opy_, bstack11l1l11_opy_ (u"ࠩࡺࠫᶦ")) as f:
          json.dump(bstack1111ll1lll1_opy_, f)
  except Exception as e:
    logger.warn(bstack11l1l11_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡸ࡯ࡣࡱࡷࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡧ࡫࡯ࡩࠥࡲ࡯ࡤ࡭࡬ࡲ࡬ࡀࠠࡼࡿࠥᶧ").format(e))
def bstack11llll1lll_opy_(bstack1llll1llll_opy_, name, logger):
  try:
    bstack11ll11ll1_opy_ = {bstack11l1l11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᶨ"): name, bstack11l1l11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᶩ"): bstack1llll1llll_opy_, bstack11l1l11_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᶪ"): str(threading.current_thread()._name)}
    return bstack11ll11ll1_opy_
  except Exception as e:
    logger.warn(bstack11l1l11_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡥࡩ࡭ࡧࡶࡦࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧ࠺ࠡࡽࢀࠦᶫ").format(e))
  return
def bstack111l1l11ll1_opy_():
    return platform.system() == bstack11l1l11_opy_ (u"ࠨ࡙࡬ࡲࡩࡵࡷࡴࠩᶬ")
def bstack11l111lll_opy_(bstack111l11ll1ll_opy_, config, logger):
    bstack1111lll1ll1_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack111l11ll1ll_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡭ࡶࡨࡶࠥࡩ࡯࡯ࡨ࡬࡫ࠥࡱࡥࡺࡵࠣࡦࡾࠦࡲࡦࡩࡨࡼࠥࡳࡡࡵࡥ࡫࠾ࠥࢁࡽࠣᶭ").format(e))
    return bstack1111lll1ll1_opy_
def bstack11l1ll11ll1_opy_(bstack111l111ll11_opy_, bstack1111llllll1_opy_):
    bstack111l1l111l1_opy_ = version.parse(bstack111l111ll11_opy_)
    bstack111l1lll111_opy_ = version.parse(bstack1111llllll1_opy_)
    if bstack111l1l111l1_opy_ > bstack111l1lll111_opy_:
        return 1
    elif bstack111l1l111l1_opy_ < bstack111l1lll111_opy_:
        return -1
    else:
        return 0
def bstack1ll1l111_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack111l1l11lll_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack111l11l1lll_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1ll111l11l_opy_(options, framework, config, bstack1l1l111111_opy_={}):
    if options is None:
        return
    if getattr(options, bstack11l1l11_opy_ (u"ࠪ࡫ࡪࡺࠧᶮ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack111lll111l_opy_ = caps.get(bstack11l1l11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᶯ"))
    bstack111l1ll11ll_opy_ = True
    bstack11llllll1_opy_ = os.environ[bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᶰ")]
    bstack1l111l1llll_opy_ = config.get(bstack11l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᶱ"), False)
    if bstack1l111l1llll_opy_:
        bstack1l1l111ll1l_opy_ = config.get(bstack11l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᶲ"), {})
        bstack1l1l111ll1l_opy_[bstack11l1l11_opy_ (u"ࠨࡣࡸࡸ࡭࡚࡯࡬ࡧࡱࠫᶳ")] = os.getenv(bstack11l1l11_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧᶴ"))
        bstack1111l1ll1ll_opy_ = json.loads(os.getenv(bstack11l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫᶵ"), bstack11l1l11_opy_ (u"ࠫࢀࢃࠧᶶ"))).get(bstack11l1l11_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᶷ"))
    if bstack111l111ll1l_opy_(caps.get(bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦ࡙࠶ࡇࠬᶸ"))) or bstack111l111ll1l_opy_(caps.get(bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡵࡴࡧࡢࡻ࠸ࡩࠧᶹ"))):
        bstack111l1ll11ll_opy_ = False
    if bstack11ll1lllll_opy_({bstack11l1l11_opy_ (u"ࠣࡷࡶࡩ࡜࠹ࡃࠣᶺ"): bstack111l1ll11ll_opy_}):
        bstack111lll111l_opy_ = bstack111lll111l_opy_ or {}
        bstack111lll111l_opy_[bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫᶻ")] = bstack111l11l1lll_opy_(framework)
        bstack111lll111l_opy_[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᶼ")] = bstack1llll11llll_opy_()
        bstack111lll111l_opy_[bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧᶽ")] = bstack11llllll1_opy_
        bstack111lll111l_opy_[bstack11l1l11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧᶾ")] = bstack1l1l111111_opy_
        if bstack1l111l1llll_opy_:
            bstack111lll111l_opy_[bstack11l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᶿ")] = bstack1l111l1llll_opy_
            bstack111lll111l_opy_[bstack11l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ᷀")] = bstack1l1l111ll1l_opy_
            bstack111lll111l_opy_[bstack11l1l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ᷁")][bstack11l1l11_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰ᷂ࠪ")] = bstack1111l1ll1ll_opy_
        if getattr(options, bstack11l1l11_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫ᷃"), None):
            options.set_capability(bstack11l1l11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ᷄"), bstack111lll111l_opy_)
        else:
            options[bstack11l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭᷅")] = bstack111lll111l_opy_
    else:
        if getattr(options, bstack11l1l11_opy_ (u"࠭ࡳࡦࡶࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹࡿࠧ᷆"), None):
            options.set_capability(bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨ᷇"), bstack111l11l1lll_opy_(framework))
            options.set_capability(bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩ᷈"), bstack1llll11llll_opy_())
            options.set_capability(bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫ᷉"), bstack11llllll1_opy_)
            options.set_capability(bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳ᷊ࠫ"), bstack1l1l111111_opy_)
            if bstack1l111l1llll_opy_:
                options.set_capability(bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ᷋"), bstack1l111l1llll_opy_)
                options.set_capability(bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ᷌"), bstack1l1l111ll1l_opy_)
                options.set_capability(bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷ࠳ࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭᷍"), bstack1111l1ll1ll_opy_)
        else:
            options[bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨ᷎")] = bstack111l11l1lll_opy_(framework)
            options[bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯᷏ࠩ")] = bstack1llll11llll_opy_()
            options[bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧ᷐ࠫ")] = bstack11llllll1_opy_
            options[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫ᷑")] = bstack1l1l111111_opy_
            if bstack1l111l1llll_opy_:
                options[bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ᷒")] = bstack1l111l1llll_opy_
                options[bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᷓ")] = bstack1l1l111ll1l_opy_
                options[bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᷔ")][bstack11l1l11_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᷕ")] = bstack1111l1ll1ll_opy_
    return options
def bstack1111lllll1l_opy_(ws_endpoint, framework):
    bstack1l1l111111_opy_ = bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠣࡒࡏࡅ࡞࡝ࡒࡊࡉࡋࡘࡤࡖࡒࡐࡆࡘࡇ࡙ࡥࡍࡂࡒࠥᷖ"))
    if ws_endpoint and len(ws_endpoint.split(bstack11l1l11_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨᷗ"))) > 1:
        ws_url = ws_endpoint.split(bstack11l1l11_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩᷘ"))[0]
        if bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧᷙ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack111l111l11l_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack11l1l11_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫᷚ"))[1]))
            bstack111l111l11l_opy_ = bstack111l111l11l_opy_ or {}
            bstack11llllll1_opy_ = os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᷛ")]
            bstack111l111l11l_opy_[bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨᷜ")] = str(framework) + str(__version__)
            bstack111l111l11l_opy_[bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᷝ")] = bstack1llll11llll_opy_()
            bstack111l111l11l_opy_[bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫᷞ")] = bstack11llllll1_opy_
            bstack111l111l11l_opy_[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫᷟ")] = bstack1l1l111111_opy_
            ws_endpoint = ws_endpoint.split(bstack11l1l11_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪᷠ"))[0] + bstack11l1l11_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫᷡ") + urllib.parse.quote(json.dumps(bstack111l111l11l_opy_))
    return ws_endpoint
def bstack1lll11ll1l_opy_():
    global bstack11l1lll1l1_opy_
    from playwright._impl._browser_type import BrowserType
    bstack11l1lll1l1_opy_ = BrowserType.connect
    return bstack11l1lll1l1_opy_
def bstack11l1ll11l1_opy_(framework_name):
    global bstack11l11l1ll_opy_
    bstack11l11l1ll_opy_ = framework_name
    return framework_name
def bstack11111ll1l1_opy_(self, *args, **kwargs):
    global bstack11l1lll1l1_opy_
    try:
        global bstack11l11l1ll_opy_
        if bstack11l1l11_opy_ (u"࠭ࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶࠪᷢ") in kwargs:
            kwargs[bstack11l1l11_opy_ (u"ࠧࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷࠫᷣ")] = bstack1111lllll1l_opy_(
                kwargs.get(bstack11l1l11_opy_ (u"ࠨࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸࠬᷤ"), None),
                bstack11l11l1ll_opy_
            )
    except Exception as e:
        logger.error(bstack11l1l11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫ࡩࡳࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡗࡉࡑࠠࡤࡣࡳࡷ࠿ࠦࡻࡾࠤᷥ").format(str(e)))
    return bstack11l1lll1l1_opy_(self, *args, **kwargs)
def bstack1111lll1111_opy_(bstack1111ll1ll11_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1l1l1l1111_opy_(bstack1111ll1ll11_opy_, bstack11l1l11_opy_ (u"ࠥࠦᷦ"))
        if proxies and proxies.get(bstack11l1l11_opy_ (u"ࠦ࡭ࡺࡴࡱࡵࠥᷧ")):
            parsed_url = urlparse(proxies.get(bstack11l1l11_opy_ (u"ࠧ࡮ࡴࡵࡲࡶࠦᷨ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack11l1l11_opy_ (u"࠭ࡰࡳࡱࡻࡽࡍࡵࡳࡵࠩᷩ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack11l1l11_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖ࡯ࡳࡶࠪᷪ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack11l1l11_opy_ (u"ࠨࡲࡵࡳࡽࡿࡕࡴࡧࡵࠫᷫ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack11l1l11_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡣࡶࡷࠬᷬ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1l11111l1_opy_(bstack1111ll1ll11_opy_):
    bstack111l1l1llll_opy_ = {
        bstack11l11lll11l_opy_[bstack111l1l1lll1_opy_]: bstack1111ll1ll11_opy_[bstack111l1l1lll1_opy_]
        for bstack111l1l1lll1_opy_ in bstack1111ll1ll11_opy_
        if bstack111l1l1lll1_opy_ in bstack11l11lll11l_opy_
    }
    bstack111l1l1llll_opy_[bstack11l1l11_opy_ (u"ࠥࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵࠥᷭ")] = bstack1111lll1111_opy_(bstack1111ll1ll11_opy_, bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠦࡵࡸ࡯ࡹࡻࡖࡩࡹࡺࡩ࡯ࡩࡶࠦᷮ")))
    bstack111l1lll11l_opy_ = [element.lower() for element in bstack11l1l111l1l_opy_]
    bstack1111l1l1l11_opy_(bstack111l1l1llll_opy_, bstack111l1lll11l_opy_)
    return bstack111l1l1llll_opy_
def bstack1111l1l1l11_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack11l1l11_opy_ (u"ࠧ࠰ࠪࠫࠬࠥᷯ")
    for value in d.values():
        if isinstance(value, dict):
            bstack1111l1l1l11_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack1111l1l1l11_opy_(item, keys)
def bstack1ll1l11ll11_opy_():
    bstack1111ll1ll1l_opy_ = [os.environ.get(bstack11l1l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡉࡍࡇࡖࡣࡉࡏࡒࠣᷰ")), os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"ࠢࡿࠤᷱ")), bstack11l1l11_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᷲ")), os.path.join(bstack11l1l11_opy_ (u"ࠩ࠲ࡸࡲࡶࠧᷳ"), bstack11l1l11_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᷴ"))]
    for path in bstack1111ll1ll1l_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack11l1l11_opy_ (u"ࠦࡋ࡯࡬ࡦࠢࠪࠦ᷵") + str(path) + bstack11l1l11_opy_ (u"ࠧ࠭ࠠࡦࡺ࡬ࡷࡹࡹ࠮ࠣ᷶"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack11l1l11_opy_ (u"ࠨࡇࡪࡸ࡬ࡲ࡬ࠦࡰࡦࡴࡰ࡭ࡸࡹࡩࡰࡰࡶࠤ࡫ࡵࡲ᷷ࠡࠩࠥ") + str(path) + bstack11l1l11_opy_ (u"ࠢࠨࠤ᷸"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack11l1l11_opy_ (u"ࠣࡈ࡬ࡰࡪ᷹ࠦࠧࠣ") + str(path) + bstack11l1l11_opy_ (u"ࠤࠪࠤࡦࡲࡲࡦࡣࡧࡽࠥ࡮ࡡࡴࠢࡷ࡬ࡪࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡤࠡࡲࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲࡸ࠴᷺ࠢ"))
            else:
                logger.debug(bstack11l1l11_opy_ (u"ࠥࡇࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧࠣࠫࠧ᷻") + str(path) + bstack11l1l11_opy_ (u"ࠦࠬࠦࡷࡪࡶ࡫ࠤࡼࡸࡩࡵࡧࠣࡴࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴ࠮ࠣ᷼"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack11l1l11_opy_ (u"ࠧࡕࡰࡦࡴࡤࡸ࡮ࡵ࡮ࠡࡵࡸࡧࡨ࡫ࡥࡥࡧࡧࠤ࡫ࡵࡲ᷽ࠡࠩࠥ") + str(path) + bstack11l1l11_opy_ (u"ࠨࠧ࠯ࠤ᷾"))
            return path
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡶࡲࠣࡪ࡮ࡲࡥࠡࠩࡾࡴࡦࡺࡨࡾࠩ࠽ࠤ᷿ࠧ") + str(e) + bstack11l1l11_opy_ (u"ࠣࠤḀ"))
    logger.debug(bstack11l1l11_opy_ (u"ࠤࡄࡰࡱࠦࡰࡢࡶ࡫ࡷࠥ࡬ࡡࡪ࡮ࡨࡨ࠳ࠨḁ"))
    return None
@measure(event_name=EVENTS.bstack11l11lllll1_opy_, stage=STAGE.bstack11l1lllll_opy_)
def bstack1l1l1lllll1_opy_(binary_path, bstack1l1l111l1ll_opy_, bs_config):
    logger.debug(bstack11l1l11_opy_ (u"ࠥࡇࡺࡸࡲࡦࡰࡷࠤࡈࡒࡉࠡࡒࡤࡸ࡭ࠦࡦࡰࡷࡱࡨ࠿ࠦࡻࡾࠤḂ").format(binary_path))
    bstack1111ll11111_opy_ = bstack11l1l11_opy_ (u"ࠫࠬḃ")
    bstack1111ll11l11_opy_ = {
        bstack11l1l11_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪḄ"): __version__,
        bstack11l1l11_opy_ (u"ࠨ࡯ࡴࠤḅ"): platform.system(),
        bstack11l1l11_opy_ (u"ࠢࡰࡵࡢࡥࡷࡩࡨࠣḆ"): platform.machine(),
        bstack11l1l11_opy_ (u"ࠣࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳࠨḇ"): bstack11l1l11_opy_ (u"ࠩ࠳ࠫḈ"),
        bstack11l1l11_opy_ (u"ࠥࡷࡩࡱ࡟࡭ࡣࡱ࡫ࡺࡧࡧࡦࠤḉ"): bstack11l1l11_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫḊ")
    }
    bstack1111ll11lll_opy_(bstack1111ll11l11_opy_)
    try:
        if binary_path:
            bstack1111ll11l11_opy_[bstack11l1l11_opy_ (u"ࠬࡩ࡬ࡪࡡࡹࡩࡷࡹࡩࡰࡰࠪḋ")] = subprocess.check_output([binary_path, bstack11l1l11_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢḌ")]).strip().decode(bstack11l1l11_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ḍ"))
        response = requests.request(
            bstack11l1l11_opy_ (u"ࠨࡉࡈࡘࠬḎ"),
            url=bstack1l11l1l1ll_opy_(bstack11l11lll1ll_opy_),
            headers=None,
            auth=(bs_config[bstack11l1l11_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫḏ")], bs_config[bstack11l1l11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭Ḑ")]),
            json=None,
            params=bstack1111ll11l11_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack11l1l11_opy_ (u"ࠫࡺࡸ࡬ࠨḑ") in data.keys() and bstack11l1l11_opy_ (u"ࠬࡻࡰࡥࡣࡷࡩࡩࡥࡣ࡭࡫ࡢࡺࡪࡸࡳࡪࡱࡱࠫḒ") in data.keys():
            logger.debug(bstack11l1l11_opy_ (u"ࠨࡎࡦࡧࡧࠤࡹࡵࠠࡶࡲࡧࡥࡹ࡫ࠠࡣ࡫ࡱࡥࡷࡿࠬࠡࡥࡸࡶࡷ࡫࡮ࡵࠢࡥ࡭ࡳࡧࡲࡺࠢࡹࡩࡷࡹࡩࡰࡰ࠽ࠤࢀࢃࠢḓ").format(bstack1111ll11l11_opy_[bstack11l1l11_opy_ (u"ࠧࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬḔ")]))
            if bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡖࡔࡏࠫḕ") in os.environ:
                logger.debug(bstack11l1l11_opy_ (u"ࠤࡖ࡯࡮ࡶࡰࡪࡰࡪࠤࡧ࡯࡮ࡢࡴࡼࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡡࡴࠢࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡗࡕࡐࠥ࡯ࡳࠡࡵࡨࡸࠧḖ"))
                data[bstack11l1l11_opy_ (u"ࠪࡹࡷࡲࠧḗ")] = os.environ[bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢ࡙ࡗࡒࠧḘ")]
            bstack1111lll1lll_opy_ = bstack111l1ll111l_opy_(data[bstack11l1l11_opy_ (u"ࠬࡻࡲ࡭ࠩḙ")], bstack1l1l111l1ll_opy_)
            bstack1111ll11111_opy_ = os.path.join(bstack1l1l111l1ll_opy_, bstack1111lll1lll_opy_)
            os.chmod(bstack1111ll11111_opy_, 0o777) # bstack1111lllll11_opy_ permission
            return bstack1111ll11111_opy_
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡱࡩࡼࠦࡓࡅࡍࠣࡿࢂࠨḚ").format(e))
    return binary_path
def bstack1111ll11lll_opy_(bstack1111ll11l11_opy_):
    try:
        if bstack11l1l11_opy_ (u"ࠧ࡭࡫ࡱࡹࡽ࠭ḛ") not in bstack1111ll11l11_opy_[bstack11l1l11_opy_ (u"ࠨࡱࡶࠫḜ")].lower():
            return
        if os.path.exists(bstack11l1l11_opy_ (u"ࠤ࠲ࡩࡹࡩ࠯ࡰࡵ࠰ࡶࡪࡲࡥࡢࡵࡨࠦḝ")):
            with open(bstack11l1l11_opy_ (u"ࠥ࠳ࡪࡺࡣ࠰ࡱࡶ࠱ࡷ࡫࡬ࡦࡣࡶࡩࠧḞ"), bstack11l1l11_opy_ (u"ࠦࡷࠨḟ")) as f:
                bstack1111l1lll11_opy_ = {}
                for line in f:
                    if bstack11l1l11_opy_ (u"ࠧࡃࠢḠ") in line:
                        key, value = line.rstrip().split(bstack11l1l11_opy_ (u"ࠨ࠽ࠣḡ"), 1)
                        bstack1111l1lll11_opy_[key] = value.strip(bstack11l1l11_opy_ (u"ࠧࠣ࡞ࠪࠫḢ"))
                bstack1111ll11l11_opy_[bstack11l1l11_opy_ (u"ࠨࡦ࡬ࡷࡹࡸ࡯ࠨḣ")] = bstack1111l1lll11_opy_.get(bstack11l1l11_opy_ (u"ࠤࡌࡈࠧḤ"), bstack11l1l11_opy_ (u"ࠥࠦḥ"))
        elif os.path.exists(bstack11l1l11_opy_ (u"ࠦ࠴࡫ࡴࡤ࠱ࡤࡰࡵ࡯࡮ࡦ࠯ࡵࡩࡱ࡫ࡡࡴࡧࠥḦ")):
            bstack1111ll11l11_opy_[bstack11l1l11_opy_ (u"ࠬࡪࡩࡴࡶࡵࡳࠬḧ")] = bstack11l1l11_opy_ (u"࠭ࡡ࡭ࡲ࡬ࡲࡪ࠭Ḩ")
    except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡺࠠࡥ࡫ࡶࡸࡷࡵࠠࡰࡨࠣࡰ࡮ࡴࡵࡹࠤḩ") + e)
@measure(event_name=EVENTS.bstack11l1l111lll_opy_, stage=STAGE.bstack11l1lllll_opy_)
def bstack111l1ll111l_opy_(bstack111l1111ll1_opy_, bstack111l1l11l1l_opy_):
    logger.debug(bstack11l1l11_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡷࡵ࡭࠻ࠢࠥḪ") + str(bstack111l1111ll1_opy_) + bstack11l1l11_opy_ (u"ࠤࠥḫ"))
    zip_path = os.path.join(bstack111l1l11l1l_opy_, bstack11l1l11_opy_ (u"ࠥࡨࡴࡽ࡮࡭ࡱࡤࡨࡪࡪ࡟ࡧ࡫࡯ࡩ࠳ࢀࡩࡱࠤḬ"))
    bstack1111lll1lll_opy_ = bstack11l1l11_opy_ (u"ࠫࠬḭ")
    with requests.get(bstack111l1111ll1_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack11l1l11_opy_ (u"ࠧࡽࡢࠣḮ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack11l1l11_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿ࠮ࠣḯ"))
    with zipfile.ZipFile(zip_path, bstack11l1l11_opy_ (u"ࠧࡳࠩḰ")) as zip_ref:
        bstack111l1ll11l1_opy_ = zip_ref.namelist()
        if len(bstack111l1ll11l1_opy_) > 0:
            bstack1111lll1lll_opy_ = bstack111l1ll11l1_opy_[0] # bstack111l11ll1l1_opy_ bstack11l1l11llll_opy_ will be bstack1lllll1l1_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack111l1l11l1l_opy_)
        logger.debug(bstack11l1l11_opy_ (u"ࠣࡈ࡬ࡰࡪࡹࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾࠦࡥࡹࡶࡵࡥࡨࡺࡥࡥࠢࡷࡳࠥ࠭ࠢḱ") + str(bstack111l1l11l1l_opy_) + bstack11l1l11_opy_ (u"ࠤࠪࠦḲ"))
    os.remove(zip_path)
    return bstack1111lll1lll_opy_
def get_cli_dir():
    bstack1111l1l1ll1_opy_ = bstack1ll1l11ll11_opy_()
    if bstack1111l1l1ll1_opy_:
        bstack1l1l111l1ll_opy_ = os.path.join(bstack1111l1l1ll1_opy_, bstack11l1l11_opy_ (u"ࠥࡧࡱ࡯ࠢḳ"))
        if not os.path.exists(bstack1l1l111l1ll_opy_):
            os.makedirs(bstack1l1l111l1ll_opy_, mode=0o777, exist_ok=True)
        return bstack1l1l111l1ll_opy_
    else:
        raise FileNotFoundError(bstack11l1l11_opy_ (u"ࠦࡓࡵࠠࡸࡴ࡬ࡸࡦࡨ࡬ࡦࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡨࡲࡶࠥࡺࡨࡦࠢࡖࡈࡐࠦࡢࡪࡰࡤࡶࡾ࠴ࠢḴ"))
def bstack1l1l1111111_opy_(bstack1l1l111l1ll_opy_):
    bstack11l1l11_opy_ (u"ࠧࠨࠢࡈࡧࡷࠤࡹ࡮ࡥࠡࡲࡤࡸ࡭ࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡓࡅࡍࠣࡦ࡮ࡴࡡࡳࡻࠣ࡭ࡳࠦࡡࠡࡹࡵ࡭ࡹࡧࡢ࡭ࡧࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾ࠴ࠢࠣࠤḵ")
    bstack111l11111ll_opy_ = [
        os.path.join(bstack1l1l111l1ll_opy_, f)
        for f in os.listdir(bstack1l1l111l1ll_opy_)
        if os.path.isfile(os.path.join(bstack1l1l111l1ll_opy_, f)) and f.startswith(bstack11l1l11_opy_ (u"ࠨࡢࡪࡰࡤࡶࡾ࠳ࠢḶ"))
    ]
    if len(bstack111l11111ll_opy_) > 0:
        return max(bstack111l11111ll_opy_, key=os.path.getmtime) # get bstack1111l1l111l_opy_ binary
    return bstack11l1l11_opy_ (u"ࠢࠣḷ")
def bstack1111ll1l11l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l1111llll1_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l1111llll1_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack111ll1l1ll_opy_(data, keys, default=None):
    bstack11l1l11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡕࡤࡪࡪࡲࡹࠡࡩࡨࡸࠥࡧࠠ࡯ࡧࡶࡸࡪࡪࠠࡷࡣ࡯ࡹࡪࠦࡦࡳࡱࡰࠤࡦࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳࡻࠣࡳࡷࠦ࡬ࡪࡵࡷ࠲ࠏࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢࡧࡥࡹࡧ࠺ࠡࡖ࡫ࡩࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺࠢࡲࡶࠥࡲࡩࡴࡶࠣࡸࡴࠦࡴࡳࡣࡹࡩࡷࡹࡥ࠯ࠌࠣࠤࠥࠦ࠺ࡱࡣࡵࡥࡲࠦ࡫ࡦࡻࡶ࠾ࠥࡇࠠ࡭࡫ࡶࡸࠥࡵࡦࠡ࡭ࡨࡽࡸ࠵ࡩ࡯ࡦ࡬ࡧࡪࡹࠠࡳࡧࡳࡶࡪࡹࡥ࡯ࡶ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡴࡦࡺࡨ࠯ࠌࠣࠤࠥࠦ࠺ࡱࡣࡵࡥࡲࠦࡤࡦࡨࡤࡹࡱࡺ࠺ࠡࡘࡤࡰࡺ࡫ࠠࡵࡱࠣࡶࡪࡺࡵࡳࡰࠣ࡭࡫ࠦࡴࡩࡧࠣࡴࡦࡺࡨࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠰ࠍࠤࠥࠦࠠ࠻ࡴࡨࡸࡺࡸ࡮࠻ࠢࡗ࡬ࡪࠦࡶࡢ࡮ࡸࡩࠥࡧࡴࠡࡶ࡫ࡩࠥࡴࡥࡴࡶࡨࡨࠥࡶࡡࡵࡪ࠯ࠤࡴࡸࠠࡥࡧࡩࡥࡺࡲࡴࠡ࡫ࡩࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪ࠮ࠋࠢࠣࠤࠥࠨࠢࠣḸ")
    if not data:
        return default
    current = data
    try:
        for key in keys:
            if isinstance(current, dict):
                current = current[key]
            elif isinstance(current, list) and isinstance(key, int):
                current = current[key]
            else:
                return default
        return current
    except (KeyError, IndexError, TypeError):
        return default