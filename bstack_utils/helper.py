# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
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
from bstack_utils.constants import (bstack1lllll1111_opy_, bstack11l1l111ll_opy_, bstack1ll1llllll_opy_,
                                    bstack11l11lllll1_opy_, bstack11l11ll11ll_opy_, bstack11l11l11l1l_opy_, bstack11l11l1l11l_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1lll1111ll_opy_, bstack1llllll11l_opy_
from bstack_utils.proxy import bstack1lll1lll11_opy_, bstack1l11l11lll_opy_
from bstack_utils.constants import *
from bstack_utils import bstack11ll1111l_opy_
from bstack_utils.bstack11l11ll111_opy_ import bstack11111lll11_opy_
from browserstack_sdk._version import __version__
bstack111ll1l1_opy_ = Config.bstack111l1111_opy_()
logger = bstack11ll1111l_opy_.get_logger(__name__, bstack11ll1111l_opy_.bstack1l11ll111l1_opy_())
def bstack111l1ll1111_opy_(config):
    return config[bstack1lll11l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪᰁ")]
def bstack111l1l1lll1_opy_(config):
    return config[bstack1lll11l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬᰂ")]
def bstack1ll1l1ll1l_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack111l1111lll_opy_(obj):
    values = []
    bstack1111l1l1l11_opy_ = re.compile(bstack1lll11l_opy_ (u"ࡵࠦࡣࡉࡕࡔࡖࡒࡑࡤ࡚ࡁࡈࡡ࡟ࡨ࠰ࠪࠢᰃ"), re.I)
    for key in obj.keys():
        if bstack1111l1l1l11_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1111lll1l11_opy_(config):
    tags = []
    tags.extend(bstack111l1111lll_opy_(os.environ))
    tags.extend(bstack111l1111lll_opy_(config))
    return tags
def bstack111l1l1111l_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111l111111l_opy_(bstack1111l1l1lll_opy_):
    if not bstack1111l1l1lll_opy_:
        return bstack1lll11l_opy_ (u"ࠫࠬᰄ")
    return bstack1lll11l_opy_ (u"ࠧࢁࡽࠡࠪࡾࢁ࠮ࠨᰅ").format(bstack1111l1l1lll_opy_.name, bstack1111l1l1lll_opy_.email)
def bstack111l11ll1l1_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111l1l1l1ll_opy_ = repo.common_dir
        info = {
            bstack1lll11l_opy_ (u"ࠨࡳࡩࡣࠥᰆ"): repo.head.commit.hexsha,
            bstack1lll11l_opy_ (u"ࠢࡴࡪࡲࡶࡹࡥࡳࡩࡣࠥᰇ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack1lll11l_opy_ (u"ࠣࡤࡵࡥࡳࡩࡨࠣᰈ"): repo.active_branch.name,
            bstack1lll11l_opy_ (u"ࠤࡷࡥ࡬ࠨᰉ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack1lll11l_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡷࡩࡷࠨᰊ"): bstack111l111111l_opy_(repo.head.commit.committer),
            bstack1lll11l_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡸࡪࡸ࡟ࡥࡣࡷࡩࠧᰋ"): repo.head.commit.committed_datetime.isoformat(),
            bstack1lll11l_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࠧᰌ"): bstack111l111111l_opy_(repo.head.commit.author),
            bstack1lll11l_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࡥࡤࡢࡶࡨࠦᰍ"): repo.head.commit.authored_datetime.isoformat(),
            bstack1lll11l_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠣᰎ"): repo.head.commit.message,
            bstack1lll11l_opy_ (u"ࠣࡴࡲࡳࡹࠨᰏ"): repo.git.rev_parse(bstack1lll11l_opy_ (u"ࠤ࠰࠱ࡸ࡮࡯ࡸ࠯ࡷࡳࡵࡲࡥࡷࡧ࡯ࠦᰐ")),
            bstack1lll11l_opy_ (u"ࠥࡧࡴࡳ࡭ࡰࡰࡢ࡫࡮ࡺ࡟ࡥ࡫ࡵࠦᰑ"): bstack111l1l1l1ll_opy_,
            bstack1lll11l_opy_ (u"ࠦࡼࡵࡲ࡬ࡶࡵࡩࡪࡥࡧࡪࡶࡢࡨ࡮ࡸࠢᰒ"): subprocess.check_output([bstack1lll11l_opy_ (u"ࠧ࡭ࡩࡵࠤᰓ"), bstack1lll11l_opy_ (u"ࠨࡲࡦࡸ࠰ࡴࡦࡸࡳࡦࠤᰔ"), bstack1lll11l_opy_ (u"ࠢ࠮࠯ࡪ࡭ࡹ࠳ࡣࡰ࡯ࡰࡳࡳ࠳ࡤࡪࡴࠥᰕ")]).strip().decode(
                bstack1lll11l_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᰖ")),
            bstack1lll11l_opy_ (u"ࠤ࡯ࡥࡸࡺ࡟ࡵࡣࡪࠦᰗ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack1lll11l_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡶࡣࡸ࡯࡮ࡤࡧࡢࡰࡦࡹࡴࡠࡶࡤ࡫ࠧᰘ"): repo.git.rev_list(
                bstack1lll11l_opy_ (u"ࠦࢀࢃ࠮࠯ࡽࢀࠦᰙ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack111l111llll_opy_ = []
        for remote in remotes:
            bstack111l11ll11l_opy_ = {
                bstack1lll11l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᰚ"): remote.name,
                bstack1lll11l_opy_ (u"ࠨࡵࡳ࡮ࠥᰛ"): remote.url,
            }
            bstack111l111llll_opy_.append(bstack111l11ll11l_opy_)
        bstack1111l1llll1_opy_ = {
            bstack1lll11l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᰜ"): bstack1lll11l_opy_ (u"ࠣࡩ࡬ࡸࠧᰝ"),
            **info,
            bstack1lll11l_opy_ (u"ࠤࡵࡩࡲࡵࡴࡦࡵࠥᰞ"): bstack111l111llll_opy_
        }
        bstack1111l1llll1_opy_ = bstack1111ll11l11_opy_(bstack1111l1llll1_opy_)
        return bstack1111l1llll1_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack1lll11l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡳࡵࡻ࡬ࡢࡶ࡬ࡲ࡬ࠦࡇࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨᰟ").format(err))
        return {}
def bstack11ll1l1ll11_opy_(bstack111l11l111l_opy_=None):
    bstack1lll11l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡌ࡫ࡴࠡࡩ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡴࡲࡨࡧ࡮࡬ࡩࡤࡣ࡯ࡰࡾࠦࡦࡰࡴࡰࡥࡹࡺࡥࡥࠢࡩࡳࡷࠦࡁࡊࠢࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠥࡻࡳࡦࠢࡦࡥࡸ࡫ࡳࠡࡨࡲࡶࠥ࡫ࡡࡤࡪࠣࡪࡴࡲࡤࡦࡴࠣ࡭ࡳࠦࡴࡩࡧࠣࡰ࡮ࡹࡴ࠯ࠌࠣࠤࠥࠦࡁࡳࡩࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡦࡰ࡮ࡧࡩࡷࡹࠠࠩ࡮࡬ࡷࡹ࠲ࠠࡰࡲࡷ࡭ࡴࡴࡡ࡭ࠫ࠽ࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡔ࡯࡯ࡧ࠽ࠤࡒࡵ࡮ࡰ࠯ࡵࡩࡵࡵࠠࡢࡲࡳࡶࡴࡧࡣࡩ࠮ࠣࡹࡸ࡫ࡳࠡࡥࡸࡶࡷ࡫࡮ࡵࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡡ࡯ࡴ࠰ࡪࡩࡹࡩࡷࡥࠪࠬࡡࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡋ࡭ࡱࡶࡼࠤࡱ࡯ࡳࡵࠢ࡞ࡡ࠿ࠦࡍࡶ࡮ࡷ࡭࠲ࡸࡥࡱࡱࠣࡥࡵࡶࡲࡰࡣࡦ࡬ࠥࡽࡩࡵࡪࠣࡲࡴࠦࡳࡰࡷࡵࡧࡪࡹࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡧࡧ࠰ࠥࡸࡥࡵࡷࡵࡲࡸ࡛ࠦ࡞ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡏ࡭ࡸࡺࠠࡰࡨࠣࡴࡦࡺࡨࡴ࠼ࠣࡑࡺࡲࡴࡪ࠯ࡵࡩࡵࡵࠠࡢࡲࡳࡶࡴࡧࡣࡩࠢࡺ࡭ࡹ࡮ࠠࡴࡲࡨࡧ࡮࡬ࡩࡤࠢࡩࡳࡱࡪࡥࡳࡵࠣࡸࡴࠦࡡ࡯ࡣ࡯ࡽࡿ࡫ࠊࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࡭࡫ࡶࡸ࠿ࠦࡌࡪࡵࡷࠤࡴ࡬ࠠࡥ࡫ࡦࡸࡸ࠲ࠠࡦࡣࡦ࡬ࠥࡩ࡯࡯ࡶࡤ࡭ࡳ࡯࡮ࡨࠢࡪ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡨࡲࡶࠥࡧࠠࡧࡱ࡯ࡨࡪࡸ࠮ࠋࠢࠣࠤࠥࠨࠢࠣᰠ")
    if bstack111l11l111l_opy_ is None:
        bstack111l11l111l_opy_ = [os.getcwd()]
    elif isinstance(bstack111l11l111l_opy_, list) and len(bstack111l11l111l_opy_) == 0:
        return []
    results = []
    for folder in bstack111l11l111l_opy_:
        try:
            if not os.path.exists(folder):
                raise Exception(bstack1lll11l_opy_ (u"ࠧࡌ࡯࡭ࡦࡨࡶࠥࡪ࡯ࡦࡵࠣࡲࡴࡺࠠࡦࡺ࡬ࡷࡹࡀࠠࡼࡿࠥᰡ").format(folder))
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack1lll11l_opy_ (u"ࠨࡰࡳࡋࡧࠦᰢ"): bstack1lll11l_opy_ (u"ࠢࠣᰣ"),
                bstack1lll11l_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢᰤ"): [],
                bstack1lll11l_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡵࠥᰥ"): [],
                bstack1lll11l_opy_ (u"ࠥࡴࡷࡊࡡࡵࡧࠥᰦ"): bstack1lll11l_opy_ (u"ࠦࠧᰧ"),
                bstack1lll11l_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡒ࡫ࡳࡴࡣࡪࡩࡸࠨᰨ"): [],
                bstack1lll11l_opy_ (u"ࠨࡰࡳࡖ࡬ࡸࡱ࡫ࠢᰩ"): bstack1lll11l_opy_ (u"ࠢࠣᰪ"),
                bstack1lll11l_opy_ (u"ࠣࡲࡵࡈࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠣᰫ"): bstack1lll11l_opy_ (u"ࠤࠥᰬ"),
                bstack1lll11l_opy_ (u"ࠥࡴࡷࡘࡡࡸࡆ࡬ࡪ࡫ࠨᰭ"): bstack1lll11l_opy_ (u"ࠦࠧᰮ")
            }
            bstack1111lll1lll_opy_ = repo.active_branch.name
            bstack1111lll1111_opy_ = repo.head.commit
            result[bstack1lll11l_opy_ (u"ࠧࡶࡲࡊࡦࠥᰯ")] = bstack1111lll1111_opy_.hexsha
            bstack1111ll1ll11_opy_ = _1111l111l1l_opy_(repo)
            logger.debug(bstack1lll11l_opy_ (u"ࠨࡂࡢࡵࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤ࡫ࡵࡲࠡࡥࡲࡱࡵࡧࡲࡪࡵࡲࡲ࠿ࠦࠢᰰ") + str(bstack1111ll1ll11_opy_) + bstack1lll11l_opy_ (u"ࠢࠣᰱ"))
            if bstack1111ll1ll11_opy_:
                try:
                    bstack111l1ll11l1_opy_ = repo.git.diff(bstack1lll11l_opy_ (u"ࠣ࠯࠰ࡲࡦࡳࡥ࠮ࡱࡱࡰࡾࠨᰲ"), bstack1lll1ll1l11_opy_ (u"ࠤࡾࡦࡦࡹࡥࡠࡤࡵࡥࡳࡩࡨࡾ࠰࠱࠲ࢀࡩࡵࡳࡴࡨࡲࡹࡥࡢࡳࡣࡱࡧ࡭ࢃࠢᰳ")).split(bstack1lll11l_opy_ (u"ࠪࡠࡳ࠭ᰴ"))
                    logger.debug(bstack1lll11l_opy_ (u"ࠦࡈ࡮ࡡ࡯ࡩࡨࡨࠥ࡬ࡩ࡭ࡧࡶࠤࡧ࡫ࡴࡸࡧࡨࡲࠥࢁࡢࡢࡵࡨࡣࡧࡸࡡ࡯ࡥ࡫ࢁࠥࡧ࡮ࡥࠢࡾࡧࡺࡸࡲࡦࡰࡷࡣࡧࡸࡡ࡯ࡥ࡫ࢁ࠿ࠦࠢᰵ") + str(bstack111l1ll11l1_opy_) + bstack1lll11l_opy_ (u"ࠧࠨᰶ"))
                    result[bstack1lll11l_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨ᰷ࠧ")] = [f.strip() for f in bstack111l1ll11l1_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1lll1ll1l11_opy_ (u"ࠢࡼࡤࡤࡷࡪࡥࡢࡳࡣࡱࡧ࡭ࢃ࠮࠯ࡽࡦࡹࡷࡸࡥ࡯ࡶࡢࡦࡷࡧ࡮ࡤࡪࢀࠦ᰸")))
                except Exception:
                    logger.debug(bstack1lll11l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡬࡫ࡴࠡࡥ࡫ࡥࡳ࡭ࡥࡥࠢࡩ࡭ࡱ࡫ࡳࠡࡨࡵࡳࡲࠦࡢࡳࡣࡱࡧ࡭ࠦࡣࡰ࡯ࡳࡥࡷ࡯ࡳࡰࡰ࠱ࠤࡋࡧ࡬࡭࡫ࡱ࡫ࠥࡨࡡࡤ࡭ࠣࡸࡴࠦࡲࡦࡥࡨࡲࡹࠦࡣࡰ࡯ࡰ࡭ࡹࡹ࠮ࠣ᰹"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack1lll11l_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣ᰺")] = _111l1l11ll1_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack1lll11l_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤ᰻")] = _111l1l11ll1_opy_(commits[:5])
            bstack111l11l1lll_opy_ = set()
            bstack111l1l111ll_opy_ = []
            for commit in commits:
                logger.debug(bstack1lll11l_opy_ (u"ࠦࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡥࡲࡱࡲ࡯ࡴ࠻ࠢࠥ᰼") + str(commit.message) + bstack1lll11l_opy_ (u"ࠧࠨ᰽"))
                bstack1111l1l111l_opy_ = commit.author.name if commit.author else bstack1lll11l_opy_ (u"ࠨࡕ࡯࡭ࡱࡳࡼࡴࠢ᰾")
                bstack111l11l1lll_opy_.add(bstack1111l1l111l_opy_)
                bstack111l1l111ll_opy_.append({
                    bstack1lll11l_opy_ (u"ࠢ࡮ࡧࡶࡷࡦ࡭ࡥࠣ᰿"): commit.message.strip(),
                    bstack1lll11l_opy_ (u"ࠣࡷࡶࡩࡷࠨ᱀"): bstack1111l1l111l_opy_
                })
            result[bstack1lll11l_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡵࠥ᱁")] = list(bstack111l11l1lll_opy_)
            result[bstack1lll11l_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡐࡩࡸࡹࡡࡨࡧࡶࠦ᱂")] = bstack111l1l111ll_opy_
            result[bstack1lll11l_opy_ (u"ࠦࡵࡸࡄࡢࡶࡨࠦ᱃")] = bstack1111lll1111_opy_.committed_datetime.strftime(bstack1lll11l_opy_ (u"࡙ࠧࠫ࠮ࠧࡰ࠱ࠪࡪࠢ᱄"))
            if (not result[bstack1lll11l_opy_ (u"ࠨࡰࡳࡖ࡬ࡸࡱ࡫ࠢ᱅")] or result[bstack1lll11l_opy_ (u"ࠢࡱࡴࡗ࡭ࡹࡲࡥࠣ᱆")].strip() == bstack1lll11l_opy_ (u"ࠣࠤ᱇")) and bstack1111lll1111_opy_.message:
                bstack111l1l1ll11_opy_ = bstack1111lll1111_opy_.message.strip().splitlines()
                result[bstack1lll11l_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥ᱈")] = bstack111l1l1ll11_opy_[0] if bstack111l1l1ll11_opy_ else bstack1lll11l_opy_ (u"ࠥࠦ᱉")
                if len(bstack111l1l1ll11_opy_) > 2:
                    result[bstack1lll11l_opy_ (u"ࠦࡵࡸࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠦ᱊")] = bstack1lll11l_opy_ (u"ࠬࡢ࡮ࠨ᱋").join(bstack111l1l1ll11_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack1lll11l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡯ࡱࡷ࡯ࡥࡹ࡯࡮ࡨࠢࡊ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡨࡲࡶࠥࡇࡉࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱࠤ࠭࡬࡯࡭ࡦࡨࡶ࠿ࠦࡻࡾࠫ࠽ࠤࢀࢃࠠ࠮ࠢࡾࢁࠧ᱌").format(
                folder,
                type(err).__name__,
                str(err)
            ))
    filtered_results = [
        result
        for result in results
        if _1111l11llll_opy_(result)
    ]
    return filtered_results
def _1111l11llll_opy_(result):
    bstack1lll11l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡉࡧ࡯ࡴࡪࡸࠠࡵࡱࠣࡧ࡭࡫ࡣ࡬ࠢ࡬ࡪࠥࡧࠠࡨ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡲࡦࡵࡸࡰࡹࠦࡩࡴࠢࡹࡥࡱ࡯ࡤࠡࠪࡱࡳࡳ࠳ࡥ࡮ࡲࡷࡽࠥ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠤࡦࡴࡤࠡࡣࡸࡸ࡭ࡵࡲࡴࠫ࠱ࠎࠥࠦࠠࠡࠤࠥࠦᱍ")
    return (
        isinstance(result.get(bstack1lll11l_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢᱎ"), None), list)
        and len(result[bstack1lll11l_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣᱏ")]) > 0
        and isinstance(result.get(bstack1lll11l_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡶࠦ᱐"), None), list)
        and len(result[bstack1lll11l_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡷࠧ᱑")]) > 0
    )
def _1111l111l1l_opy_(repo):
    bstack1lll11l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤ࡚ࠥࡲࡺࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡶ࡫ࡩࠥࡨࡡࡴࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡪࡴࡸࠠࡵࡪࡨࠤ࡬࡯ࡶࡦࡰࠣࡶࡪࡶ࡯ࠡࡹ࡬ࡸ࡭ࡵࡵࡵࠢ࡫ࡥࡷࡪࡣࡰࡦࡨࡨࠥࡴࡡ࡮ࡧࡶࠤࡦࡴࡤࠡࡹࡲࡶࡰࠦࡷࡪࡶ࡫ࠤࡦࡲ࡬ࠡࡘࡆࡗࠥࡶࡲࡰࡸ࡬ࡨࡪࡸࡳ࠯ࠌࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹࠠࡵࡪࡨࠤࡩ࡫ࡦࡢࡷ࡯ࡸࠥࡨࡲࡢࡰࡦ࡬ࠥ࡯ࡦࠡࡲࡲࡷࡸ࡯ࡢ࡭ࡧ࠯ࠤࡪࡲࡳࡦࠢࡑࡳࡳ࡫࠮ࠋࠢࠣࠤࠥࠨࠢࠣ᱒")
    try:
        try:
            origin = repo.remotes.origin
            bstack1111ll1llll_opy_ = origin.refs[bstack1lll11l_opy_ (u"࠭ࡈࡆࡃࡇࠫ᱓")]
            target = bstack1111ll1llll_opy_.reference.name
            if target.startswith(bstack1lll11l_opy_ (u"ࠧࡰࡴ࡬࡫࡮ࡴ࠯ࠨ᱔")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack1lll11l_opy_ (u"ࠨࡱࡵ࡭࡬࡯࡮࠰ࠩ᱕")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _111l1l11ll1_opy_(commits):
    bstack1lll11l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡊࡩࡹࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡤࡪࡤࡲ࡬࡫ࡤࠡࡨ࡬ࡰࡪࡹࠠࡧࡴࡲࡱࠥࡧࠠ࡭࡫ࡶࡸࠥࡵࡦࠡࡥࡲࡱࡲ࡯ࡴࡴ࠰ࠍࠤࠥࠦࠠࠣࠤࠥ᱖")
    bstack111l1ll11l1_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack111l1l11lll_opy_ in diff:
                        if bstack111l1l11lll_opy_.a_path:
                            bstack111l1ll11l1_opy_.add(bstack111l1l11lll_opy_.a_path)
                        if bstack111l1l11lll_opy_.b_path:
                            bstack111l1ll11l1_opy_.add(bstack111l1l11lll_opy_.b_path)
    except Exception:
        pass
    return list(bstack111l1ll11l1_opy_)
def bstack1111ll11l11_opy_(bstack1111l1llll1_opy_):
    bstack111l111l111_opy_ = bstack111l1ll1l11_opy_(bstack1111l1llll1_opy_)
    if bstack111l111l111_opy_ and bstack111l111l111_opy_ > bstack11l11lllll1_opy_:
        bstack1111ll11lll_opy_ = bstack111l111l111_opy_ - bstack11l11lllll1_opy_
        bstack111l11lll11_opy_ = bstack1111l11ll11_opy_(bstack1111l1llll1_opy_[bstack1lll11l_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡢࡱࡪࡹࡳࡢࡩࡨࠦ᱗")], bstack1111ll11lll_opy_)
        bstack1111l1llll1_opy_[bstack1lll11l_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧ᱘")] = bstack111l11lll11_opy_
        logger.info(bstack1lll11l_opy_ (u"࡚ࠧࡨࡦࠢࡦࡳࡲࡳࡩࡵࠢ࡫ࡥࡸࠦࡢࡦࡧࡱࠤࡹࡸࡵ࡯ࡥࡤࡸࡪࡪ࠮ࠡࡕ࡬ࡾࡪࠦ࡯ࡧࠢࡦࡳࡲࡳࡩࡵࠢࡤࡪࡹ࡫ࡲࠡࡶࡵࡹࡳࡩࡡࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡽࢀࠤࡐࡈࠢ᱙")
                    .format(bstack111l1ll1l11_opy_(bstack1111l1llll1_opy_) / 1024))
    return bstack1111l1llll1_opy_
def bstack111l1ll1l11_opy_(json_data):
    try:
        if json_data:
            bstack1111lll11l1_opy_ = json.dumps(json_data)
            bstack1111ll111ll_opy_ = sys.getsizeof(bstack1111lll11l1_opy_)
            return bstack1111ll111ll_opy_
    except Exception as e:
        logger.debug(bstack1lll11l_opy_ (u"ࠨࡓࡰ࡯ࡨࡸ࡭࡯࡮ࡨࠢࡺࡩࡳࡺࠠࡸࡴࡲࡲ࡬ࠦࡷࡩ࡫࡯ࡩࠥࡩࡡ࡭ࡥࡸࡰࡦࡺࡩ࡯ࡩࠣࡷ࡮ࢀࡥࠡࡱࡩࠤࡏ࡙ࡏࡏࠢࡲࡦ࡯࡫ࡣࡵ࠼ࠣࡿࢂࠨᱚ").format(e))
    return -1
def bstack1111l11ll11_opy_(field, bstack1111l111ll1_opy_):
    try:
        bstack111l1l111l1_opy_ = len(bytes(bstack11l11ll11ll_opy_, bstack1lll11l_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᱛ")))
        bstack1111ll11111_opy_ = bytes(field, bstack1lll11l_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᱜ"))
        bstack111l11l1111_opy_ = len(bstack1111ll11111_opy_)
        bstack111l111l1l1_opy_ = ceil(bstack111l11l1111_opy_ - bstack1111l111ll1_opy_ - bstack111l1l111l1_opy_)
        if bstack111l111l1l1_opy_ > 0:
            bstack1111ll1lll1_opy_ = bstack1111ll11111_opy_[:bstack111l111l1l1_opy_].decode(bstack1lll11l_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᱝ"), errors=bstack1lll11l_opy_ (u"ࠪ࡭࡬ࡴ࡯ࡳࡧࠪᱞ")) + bstack11l11ll11ll_opy_
            return bstack1111ll1lll1_opy_
    except Exception as e:
        logger.debug(bstack1lll11l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡷࡶࡺࡴࡣࡢࡶ࡬ࡲ࡬ࠦࡦࡪࡧ࡯ࡨ࠱ࠦ࡮ࡰࡶ࡫࡭ࡳ࡭ࠠࡸࡣࡶࠤࡹࡸࡵ࡯ࡥࡤࡸࡪࡪࠠࡩࡧࡵࡩ࠿ࠦࡻࡾࠤᱟ").format(e))
    return field
def bstack11l1lllll1_opy_():
    env = os.environ
    if (bstack1lll11l_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡕࡓࡎࠥᱠ") in env and len(env[bstack1lll11l_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡖࡔࡏࠦᱡ")]) > 0) or (
            bstack1lll11l_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡊࡒࡑࡊࠨᱢ") in env and len(env[bstack1lll11l_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡋࡓࡒࡋࠢᱣ")]) > 0):
        return {
            bstack1lll11l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᱤ"): bstack1lll11l_opy_ (u"ࠥࡎࡪࡴ࡫ࡪࡰࡶࠦᱥ"),
            bstack1lll11l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᱦ"): env.get(bstack1lll11l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᱧ")),
            bstack1lll11l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᱨ"): env.get(bstack1lll11l_opy_ (u"ࠢࡋࡑࡅࡣࡓࡇࡍࡆࠤᱩ")),
            bstack1lll11l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᱪ"): env.get(bstack1lll11l_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᱫ"))
        }
    if env.get(bstack1lll11l_opy_ (u"ࠥࡇࡎࠨᱬ")) == bstack1lll11l_opy_ (u"ࠦࡹࡸࡵࡦࠤᱭ") and bstack111llll1l_opy_(env.get(bstack1lll11l_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡈࡏࠢᱮ"))):
        return {
            bstack1lll11l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᱯ"): bstack1lll11l_opy_ (u"ࠢࡄ࡫ࡵࡧࡱ࡫ࡃࡊࠤᱰ"),
            bstack1lll11l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᱱ"): env.get(bstack1lll11l_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᱲ")),
            bstack1lll11l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᱳ"): env.get(bstack1lll11l_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡣࡏࡕࡂࠣᱴ")),
            bstack1lll11l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᱵ"): env.get(bstack1lll11l_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࠤᱶ"))
        }
    if env.get(bstack1lll11l_opy_ (u"ࠢࡄࡋࠥᱷ")) == bstack1lll11l_opy_ (u"ࠣࡶࡵࡹࡪࠨᱸ") and bstack111llll1l_opy_(env.get(bstack1lll11l_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࠤᱹ"))):
        return {
            bstack1lll11l_opy_ (u"ࠥࡲࡦࡳࡥࠣᱺ"): bstack1lll11l_opy_ (u"࡙ࠦࡸࡡࡷ࡫ࡶࠤࡈࡏࠢᱻ"),
            bstack1lll11l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᱼ"): env.get(bstack1lll11l_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡂࡖࡋࡏࡈࡤ࡝ࡅࡃࡡࡘࡖࡑࠨᱽ")),
            bstack1lll11l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᱾"): env.get(bstack1lll11l_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥ᱿")),
            bstack1lll11l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲀ"): env.get(bstack1lll11l_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᲁ"))
        }
    if env.get(bstack1lll11l_opy_ (u"ࠦࡈࡏࠢᲂ")) == bstack1lll11l_opy_ (u"ࠧࡺࡲࡶࡧࠥᲃ") and env.get(bstack1lll11l_opy_ (u"ࠨࡃࡊࡡࡑࡅࡒࡋࠢᲄ")) == bstack1lll11l_opy_ (u"ࠢࡤࡱࡧࡩࡸ࡮ࡩࡱࠤᲅ"):
        return {
            bstack1lll11l_opy_ (u"ࠣࡰࡤࡱࡪࠨᲆ"): bstack1lll11l_opy_ (u"ࠤࡆࡳࡩ࡫ࡳࡩ࡫ࡳࠦᲇ"),
            bstack1lll11l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᲈ"): None,
            bstack1lll11l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲉ"): None,
            bstack1lll11l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᲊ"): None
        }
    if env.get(bstack1lll11l_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡅࡖࡆࡔࡃࡉࠤ᲋")) and env.get(bstack1lll11l_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡇࡔࡓࡍࡊࡖࠥ᲌")):
        return {
            bstack1lll11l_opy_ (u"ࠣࡰࡤࡱࡪࠨ᲍"): bstack1lll11l_opy_ (u"ࠤࡅ࡭ࡹࡨࡵࡤ࡭ࡨࡸࠧ᲎"),
            bstack1lll11l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᲏"): env.get(bstack1lll11l_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡈࡋࡗࡣࡍ࡚ࡔࡑࡡࡒࡖࡎࡍࡉࡏࠤᲐ")),
            bstack1lll11l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᲑ"): None,
            bstack1lll11l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᲒ"): env.get(bstack1lll11l_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᲓ"))
        }
    if env.get(bstack1lll11l_opy_ (u"ࠣࡅࡌࠦᲔ")) == bstack1lll11l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᲕ") and bstack111llll1l_opy_(env.get(bstack1lll11l_opy_ (u"ࠥࡈࡗࡕࡎࡆࠤᲖ"))):
        return {
            bstack1lll11l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲗ"): bstack1lll11l_opy_ (u"ࠧࡊࡲࡰࡰࡨࠦᲘ"),
            bstack1lll11l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᲙ"): env.get(bstack1lll11l_opy_ (u"ࠢࡅࡔࡒࡒࡊࡥࡂࡖࡋࡏࡈࡤࡒࡉࡏࡍࠥᲚ")),
            bstack1lll11l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲛ"): None,
            bstack1lll11l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲜ"): env.get(bstack1lll11l_opy_ (u"ࠥࡈࡗࡕࡎࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᲝ"))
        }
    if env.get(bstack1lll11l_opy_ (u"ࠦࡈࡏࠢᲞ")) == bstack1lll11l_opy_ (u"ࠧࡺࡲࡶࡧࠥᲟ") and bstack111llll1l_opy_(env.get(bstack1lll11l_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࠤᲠ"))):
        return {
            bstack1lll11l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲡ"): bstack1lll11l_opy_ (u"ࠣࡕࡨࡱࡦࡶࡨࡰࡴࡨࠦᲢ"),
            bstack1lll11l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲣ"): env.get(bstack1lll11l_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡏࡓࡉࡄࡒࡎࡠࡁࡕࡋࡒࡒࡤ࡛ࡒࡍࠤᲤ")),
            bstack1lll11l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲥ"): env.get(bstack1lll11l_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᲦ")),
            bstack1lll11l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᲧ"): env.get(bstack1lll11l_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡎࡔࡈ࡟ࡊࡆࠥᲨ"))
        }
    if env.get(bstack1lll11l_opy_ (u"ࠣࡅࡌࠦᲩ")) == bstack1lll11l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᲪ") and bstack111llll1l_opy_(env.get(bstack1lll11l_opy_ (u"ࠥࡋࡎ࡚ࡌࡂࡄࡢࡇࡎࠨᲫ"))):
        return {
            bstack1lll11l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲬ"): bstack1lll11l_opy_ (u"ࠧࡍࡩࡵࡎࡤࡦࠧᲭ"),
            bstack1lll11l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᲮ"): env.get(bstack1lll11l_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡖࡔࡏࠦᲯ")),
            bstack1lll11l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲰ"): env.get(bstack1lll11l_opy_ (u"ࠤࡆࡍࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᲱ")),
            bstack1lll11l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᲲ"): env.get(bstack1lll11l_opy_ (u"ࠦࡈࡏ࡟ࡋࡑࡅࡣࡎࡊࠢᲳ"))
        }
    if env.get(bstack1lll11l_opy_ (u"ࠧࡉࡉࠣᲴ")) == bstack1lll11l_opy_ (u"ࠨࡴࡳࡷࡨࠦᲵ") and bstack111llll1l_opy_(env.get(bstack1lll11l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࠥᲶ"))):
        return {
            bstack1lll11l_opy_ (u"ࠣࡰࡤࡱࡪࠨᲷ"): bstack1lll11l_opy_ (u"ࠤࡅࡹ࡮ࡲࡤ࡬࡫ࡷࡩࠧᲸ"),
            bstack1lll11l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᲹ"): env.get(bstack1lll11l_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᲺ")),
            bstack1lll11l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᲻"): env.get(bstack1lll11l_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡏࡅࡇࡋࡌࠣ᲼")) or env.get(bstack1lll11l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤࡔࡁࡎࡇࠥᲽ")),
            bstack1lll11l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᲾ"): env.get(bstack1lll11l_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᲿ"))
        }
    if bstack111llll1l_opy_(env.get(bstack1lll11l_opy_ (u"ࠥࡘࡋࡥࡂࡖࡋࡏࡈࠧ᳀"))):
        return {
            bstack1lll11l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᳁"): bstack1lll11l_opy_ (u"ࠧ࡜ࡩࡴࡷࡤࡰ࡙ࠥࡴࡶࡦ࡬ࡳ࡚ࠥࡥࡢ࡯ࠣࡗࡪࡸࡶࡪࡥࡨࡷࠧ᳂"),
            bstack1lll11l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᳃"): bstack1lll11l_opy_ (u"ࠢࡼࡿࡾࢁࠧ᳄").format(env.get(bstack1lll11l_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡌࡏࡖࡐࡇࡅ࡙ࡏࡏࡏࡕࡈࡖ࡛ࡋࡒࡖࡔࡌࠫ᳅")), env.get(bstack1lll11l_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡐࡓࡑࡍࡉࡈ࡚ࡉࡅࠩ᳆"))),
            bstack1lll11l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᳇"): env.get(bstack1lll11l_opy_ (u"ࠦࡘ࡟ࡓࡕࡇࡐࡣࡉࡋࡆࡊࡐࡌࡘࡎࡕࡎࡊࡆࠥ᳈")),
            bstack1lll11l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᳉"): env.get(bstack1lll11l_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉࠨ᳊"))
        }
    if bstack111llll1l_opy_(env.get(bstack1lll11l_opy_ (u"ࠢࡂࡒࡓ࡚ࡊ࡟ࡏࡓࠤ᳋"))):
        return {
            bstack1lll11l_opy_ (u"ࠣࡰࡤࡱࡪࠨ᳌"): bstack1lll11l_opy_ (u"ࠤࡄࡴࡵࡼࡥࡺࡱࡵࠦ᳍"),
            bstack1lll11l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᳎"): bstack1lll11l_opy_ (u"ࠦࢀࢃ࠯ࡱࡴࡲ࡮ࡪࡩࡴ࠰ࡽࢀ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿࠥ᳏").format(env.get(bstack1lll11l_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡖࡔࡏࠫ᳐")), env.get(bstack1lll11l_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡃࡆࡇࡔ࡛ࡎࡕࡡࡑࡅࡒࡋࠧ᳑")), env.get(bstack1lll11l_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡓࡖࡔࡐࡅࡄࡖࡢࡗࡑ࡛ࡇࠨ᳒")), env.get(bstack1lll11l_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬ᳓"))),
            bstack1lll11l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨ᳔ࠦ"): env.get(bstack1lll11l_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡐࡏࡃࡡࡑࡅࡒࡋ᳕ࠢ")),
            bstack1lll11l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴ᳖ࠥ"): env.get(bstack1lll11l_opy_ (u"ࠧࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨ᳗"))
        }
    if env.get(bstack1lll11l_opy_ (u"ࠨࡁ࡛ࡗࡕࡉࡤࡎࡔࡕࡒࡢ࡙ࡘࡋࡒࡠࡃࡊࡉࡓ࡚᳘ࠢ")) and env.get(bstack1lll11l_opy_ (u"ࠢࡕࡈࡢࡆ࡚ࡏࡌࡅࠤ᳙")):
        return {
            bstack1lll11l_opy_ (u"ࠣࡰࡤࡱࡪࠨ᳚"): bstack1lll11l_opy_ (u"ࠤࡄࡾࡺࡸࡥࠡࡅࡌࠦ᳛"),
            bstack1lll11l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᳜"): bstack1lll11l_opy_ (u"ࠦࢀࢃࡻࡾ࠱ࡢࡦࡺ࡯࡬ࡥ࠱ࡵࡩࡸࡻ࡬ࡵࡵࡂࡦࡺ࡯࡬ࡥࡋࡧࡁࢀࢃ᳝ࠢ").format(env.get(bstack1lll11l_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡉࡓ࡚ࡔࡄࡂࡖࡌࡓࡓ࡙ࡅࡓࡘࡈࡖ࡚ࡘࡉࠨ᳞")), env.get(bstack1lll11l_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡔࡗࡕࡊࡆࡅࡗ᳟ࠫ")), env.get(bstack1lll11l_opy_ (u"ࠧࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠧ᳠"))),
            bstack1lll11l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᳡"): env.get(bstack1lll11l_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤ᳢")),
            bstack1lll11l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳣"): env.get(bstack1lll11l_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇ᳤ࠦ"))
        }
    if any([env.get(bstack1lll11l_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆ᳥ࠥ")), env.get(bstack1lll11l_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡕࡉࡘࡕࡌࡗࡇࡇࡣࡘࡕࡕࡓࡅࡈࡣ࡛ࡋࡒࡔࡋࡒࡒ᳦ࠧ")), env.get(bstack1lll11l_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡗࡔ࡛ࡒࡄࡇࡢ࡚ࡊࡘࡓࡊࡑࡑ᳧ࠦ"))]):
        return {
            bstack1lll11l_opy_ (u"ࠣࡰࡤࡱࡪࠨ᳨"): bstack1lll11l_opy_ (u"ࠤࡄ࡛ࡘࠦࡃࡰࡦࡨࡆࡺ࡯࡬ࡥࠤᳩ"),
            bstack1lll11l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᳪ"): env.get(bstack1lll11l_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡑࡗࡅࡐࡎࡉ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᳫ")),
            bstack1lll11l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᳬ"): env.get(bstack1lll11l_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇ᳭ࠦ")),
            bstack1lll11l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᳮ"): env.get(bstack1lll11l_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᳯ"))
        }
    if env.get(bstack1lll11l_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡏࡷࡰࡦࡪࡸࠢᳰ")):
        return {
            bstack1lll11l_opy_ (u"ࠥࡲࡦࡳࡥࠣᳱ"): bstack1lll11l_opy_ (u"ࠦࡇࡧ࡭ࡣࡱࡲࠦᳲ"),
            bstack1lll11l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᳳ"): env.get(bstack1lll11l_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡗ࡫ࡳࡶ࡮ࡷࡷ࡚ࡸ࡬ࠣ᳴")),
            bstack1lll11l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᳵ"): env.get(bstack1lll11l_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡵ࡫ࡳࡷࡺࡊࡰࡤࡑࡥࡲ࡫ࠢᳶ")),
            bstack1lll11l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᳷"): env.get(bstack1lll11l_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡐࡸࡱࡧ࡫ࡲࠣ᳸"))
        }
    if env.get(bstack1lll11l_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࠧ᳹")) or env.get(bstack1lll11l_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡍࡂࡋࡑࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡓࡕࡃࡕࡘࡊࡊࠢᳺ")):
        return {
            bstack1lll11l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᳻"): bstack1lll11l_opy_ (u"ࠢࡘࡧࡵࡧࡰ࡫ࡲࠣ᳼"),
            bstack1lll11l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᳽"): env.get(bstack1lll11l_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨ᳾")),
            bstack1lll11l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᳿"): bstack1lll11l_opy_ (u"ࠦࡒࡧࡩ࡯ࠢࡓ࡭ࡵ࡫࡬ࡪࡰࡨࠦᴀ") if env.get(bstack1lll11l_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡍࡂࡋࡑࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡓࡕࡃࡕࡘࡊࡊࠢᴁ")) else None,
            bstack1lll11l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴂ"): env.get(bstack1lll11l_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡉࡌࡘࡤࡉࡏࡎࡏࡌࡘࠧᴃ"))
        }
    if any([env.get(bstack1lll11l_opy_ (u"ࠣࡉࡆࡔࡤࡖࡒࡐࡌࡈࡇ࡙ࠨᴄ")), env.get(bstack1lll11l_opy_ (u"ࠤࡊࡇࡑࡕࡕࡅࡡࡓࡖࡔࡐࡅࡄࡖࠥᴅ")), env.get(bstack1lll11l_opy_ (u"ࠥࡋࡔࡕࡇࡍࡇࡢࡇࡑࡕࡕࡅࡡࡓࡖࡔࡐࡅࡄࡖࠥᴆ"))]):
        return {
            bstack1lll11l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᴇ"): bstack1lll11l_opy_ (u"ࠧࡍ࡯ࡰࡩ࡯ࡩࠥࡉ࡬ࡰࡷࡧࠦᴈ"),
            bstack1lll11l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᴉ"): None,
            bstack1lll11l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᴊ"): env.get(bstack1lll11l_opy_ (u"ࠣࡒࡕࡓࡏࡋࡃࡕࡡࡌࡈࠧᴋ")),
            bstack1lll11l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᴌ"): env.get(bstack1lll11l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᴍ"))
        }
    if env.get(bstack1lll11l_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋࠢᴎ")):
        return {
            bstack1lll11l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴏ"): bstack1lll11l_opy_ (u"ࠨࡓࡩ࡫ࡳࡴࡦࡨ࡬ࡦࠤᴐ"),
            bstack1lll11l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴑ"): env.get(bstack1lll11l_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᴒ")),
            bstack1lll11l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᴓ"): bstack1lll11l_opy_ (u"ࠥࡎࡴࡨࠠࠤࡽࢀࠦᴔ").format(env.get(bstack1lll11l_opy_ (u"ࠫࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡋࡑࡅࡣࡎࡊࠧᴕ"))) if env.get(bstack1lll11l_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࡠࡌࡒࡆࡤࡏࡄࠣᴖ")) else None,
            bstack1lll11l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴗ"): env.get(bstack1lll11l_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᴘ"))
        }
    if bstack111llll1l_opy_(env.get(bstack1lll11l_opy_ (u"ࠣࡐࡈࡘࡑࡏࡆ࡚ࠤᴙ"))):
        return {
            bstack1lll11l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᴚ"): bstack1lll11l_opy_ (u"ࠥࡒࡪࡺ࡬ࡪࡨࡼࠦᴛ"),
            bstack1lll11l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴜ"): env.get(bstack1lll11l_opy_ (u"ࠧࡊࡅࡑࡎࡒ࡝ࡤ࡛ࡒࡍࠤᴝ")),
            bstack1lll11l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴞ"): env.get(bstack1lll11l_opy_ (u"ࠢࡔࡋࡗࡉࡤࡔࡁࡎࡇࠥᴟ")),
            bstack1lll11l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴠ"): env.get(bstack1lll11l_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᴡ"))
        }
    if bstack111llll1l_opy_(env.get(bstack1lll11l_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢࡅࡈ࡚ࡉࡐࡐࡖࠦᴢ"))):
        return {
            bstack1lll11l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᴣ"): bstack1lll11l_opy_ (u"ࠧࡍࡩࡵࡊࡸࡦࠥࡇࡣࡵ࡫ࡲࡲࡸࠨᴤ"),
            bstack1lll11l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᴥ"): bstack1lll11l_opy_ (u"ࠢࡼࡿ࠲ࡿࢂ࠵ࡡࡤࡶ࡬ࡳࡳࡹ࠯ࡳࡷࡱࡷ࠴ࢁࡽࠣᴦ").format(env.get(bstack1lll11l_opy_ (u"ࠨࡉࡌࡘࡍ࡛ࡂࡠࡕࡈࡖ࡛ࡋࡒࡠࡗࡕࡐࠬᴧ")), env.get(bstack1lll11l_opy_ (u"ࠩࡊࡍ࡙ࡎࡕࡃࡡࡕࡉࡕࡕࡓࡊࡖࡒࡖ࡞࠭ᴨ")), env.get(bstack1lll11l_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡖ࡚ࡔ࡟ࡊࡆࠪᴩ"))),
            bstack1lll11l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴪ"): env.get(bstack1lll11l_opy_ (u"ࠧࡍࡉࡕࡊࡘࡆࡤ࡝ࡏࡓࡍࡉࡐࡔ࡝ࠢᴫ")),
            bstack1lll11l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴬ"): env.get(bstack1lll11l_opy_ (u"ࠢࡈࡋࡗࡌ࡚ࡈ࡟ࡓࡗࡑࡣࡎࡊࠢᴭ"))
        }
    if env.get(bstack1lll11l_opy_ (u"ࠣࡅࡌࠦᴮ")) == bstack1lll11l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᴯ") and env.get(bstack1lll11l_opy_ (u"࡚ࠥࡊࡘࡃࡆࡎࠥᴰ")) == bstack1lll11l_opy_ (u"ࠦ࠶ࠨᴱ"):
        return {
            bstack1lll11l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴲ"): bstack1lll11l_opy_ (u"ࠨࡖࡦࡴࡦࡩࡱࠨᴳ"),
            bstack1lll11l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴴ"): bstack1lll11l_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࡽࢀࠦᴵ").format(env.get(bstack1lll11l_opy_ (u"࡙ࠩࡉࡗࡉࡅࡍࡡࡘࡖࡑ࠭ᴶ"))),
            bstack1lll11l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴷ"): None,
            bstack1lll11l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᴸ"): None,
        }
    if env.get(bstack1lll11l_opy_ (u"࡚ࠧࡅࡂࡏࡆࡍ࡙࡟࡟ࡗࡇࡕࡗࡎࡕࡎࠣᴹ")):
        return {
            bstack1lll11l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᴺ"): bstack1lll11l_opy_ (u"ࠢࡕࡧࡤࡱࡨ࡯ࡴࡺࠤᴻ"),
            bstack1lll11l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᴼ"): None,
            bstack1lll11l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᴽ"): env.get(bstack1lll11l_opy_ (u"ࠥࡘࡊࡇࡍࡄࡋࡗ࡝ࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡎࡂࡏࡈࠦᴾ")),
            bstack1lll11l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᴿ"): env.get(bstack1lll11l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᵀ"))
        }
    if any([env.get(bstack1lll11l_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࠤᵁ")), env.get(bstack1lll11l_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࡢ࡙ࡗࡒࠢᵂ")), env.get(bstack1lll11l_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࡣ࡚࡙ࡅࡓࡐࡄࡑࡊࠨᵃ")), env.get(bstack1lll11l_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡚ࡅࡂࡏࠥᵄ"))]):
        return {
            bstack1lll11l_opy_ (u"ࠥࡲࡦࡳࡥࠣᵅ"): bstack1lll11l_opy_ (u"ࠦࡈࡵ࡮ࡤࡱࡸࡶࡸ࡫ࠢᵆ"),
            bstack1lll11l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᵇ"): None,
            bstack1lll11l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᵈ"): env.get(bstack1lll11l_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᵉ")) or None,
            bstack1lll11l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᵊ"): env.get(bstack1lll11l_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᵋ"), 0)
        }
    if env.get(bstack1lll11l_opy_ (u"ࠥࡋࡔࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᵌ")):
        return {
            bstack1lll11l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᵍ"): bstack1lll11l_opy_ (u"ࠧࡍ࡯ࡄࡆࠥᵎ"),
            bstack1lll11l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᵏ"): None,
            bstack1lll11l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᵐ"): env.get(bstack1lll11l_opy_ (u"ࠣࡉࡒࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᵑ")),
            bstack1lll11l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᵒ"): env.get(bstack1lll11l_opy_ (u"ࠥࡋࡔࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡅࡒ࡙ࡓ࡚ࡅࡓࠤᵓ"))
        }
    if env.get(bstack1lll11l_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤᵔ")):
        return {
            bstack1lll11l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᵕ"): bstack1lll11l_opy_ (u"ࠨࡃࡰࡦࡨࡊࡷ࡫ࡳࡩࠤᵖ"),
            bstack1lll11l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᵗ"): env.get(bstack1lll11l_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᵘ")),
            bstack1lll11l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᵙ"): env.get(bstack1lll11l_opy_ (u"ࠥࡇࡋࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡐࡄࡑࡊࠨᵚ")),
            bstack1lll11l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᵛ"): env.get(bstack1lll11l_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᵜ"))
        }
    return {bstack1lll11l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᵝ"): None}
def get_host_info():
    return {
        bstack1lll11l_opy_ (u"ࠢࡩࡱࡶࡸࡳࡧ࡭ࡦࠤᵞ"): platform.node(),
        bstack1lll11l_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠥᵟ"): platform.system(),
        bstack1lll11l_opy_ (u"ࠤࡷࡽࡵ࡫ࠢᵠ"): platform.machine(),
        bstack1lll11l_opy_ (u"ࠥࡺࡪࡸࡳࡪࡱࡱࠦᵡ"): platform.version(),
        bstack1lll11l_opy_ (u"ࠦࡦࡸࡣࡩࠤᵢ"): platform.architecture()[0]
    }
def bstack111l1ll11_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack1111l11lll1_opy_():
    if bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭ᵣ")):
        return bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᵤ")
    return bstack1lll11l_opy_ (u"ࠧࡶࡰ࡮ࡲࡴࡽ࡮ࡠࡩࡵ࡭ࡩ࠭ᵥ")
def bstack1111llll111_opy_(driver):
    info = {
        bstack1lll11l_opy_ (u"ࠨࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧᵦ"): driver.capabilities,
        bstack1lll11l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩ࠭ᵧ"): driver.session_id,
        bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫᵨ"): driver.capabilities.get(bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩᵩ"), None),
        bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᵪ"): driver.capabilities.get(bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᵫ"), None),
        bstack1lll11l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᵬ"): driver.capabilities.get(bstack1lll11l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧᵭ"), None),
        bstack1lll11l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᵮ"):driver.capabilities.get(bstack1lll11l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᵯ"), None),
    }
    if bstack1111l11lll1_opy_() == bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᵰ"):
        if bstack1l1ll1lll_opy_():
            info[bstack1lll11l_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᵱ")] = bstack1lll11l_opy_ (u"࠭ࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᵲ")
        elif driver.capabilities.get(bstack1lll11l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᵳ"), {}).get(bstack1lll11l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬᵴ"), False):
            info[bstack1lll11l_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࠪᵵ")] = bstack1lll11l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧᵶ")
        else:
            info[bstack1lll11l_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬᵷ")] = bstack1lll11l_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᵸ")
    return info
def bstack1l1ll1lll_opy_():
    if bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᵹ")):
        return True
    if bstack111llll1l_opy_(os.environ.get(bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨᵺ"), None)):
        return True
    return False
def bstack1l11l1111_opy_(bstack1111ll1l1l1_opy_, url, data, config):
    headers = config.get(bstack1lll11l_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩᵻ"), None)
    proxies = bstack1lll1lll11_opy_(config, url)
    auth = config.get(bstack1lll11l_opy_ (u"ࠩࡤࡹࡹ࡮ࠧᵼ"), None)
    response = requests.request(
            bstack1111ll1l1l1_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack11111ll111_opy_(bstack1lll1ll11l_opy_, size):
    bstack1l1l1l1lll_opy_ = []
    while len(bstack1lll1ll11l_opy_) > size:
        bstack1l1lllllll_opy_ = bstack1lll1ll11l_opy_[:size]
        bstack1l1l1l1lll_opy_.append(bstack1l1lllllll_opy_)
        bstack1lll1ll11l_opy_ = bstack1lll1ll11l_opy_[size:]
    bstack1l1l1l1lll_opy_.append(bstack1lll1ll11l_opy_)
    return bstack1l1l1l1lll_opy_
def bstack1111llll11l_opy_(message, bstack111l11111ll_opy_=False):
    os.write(1, bytes(message, bstack1lll11l_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᵽ")))
    os.write(1, bytes(bstack1lll11l_opy_ (u"ࠫࡡࡴࠧᵾ"), bstack1lll11l_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᵿ")))
    if bstack111l11111ll_opy_:
        with open(bstack1lll11l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࠳࡯࠲࠳ࡼ࠱ࠬᶀ") + os.environ[bstack1lll11l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭ᶁ")] + bstack1lll11l_opy_ (u"ࠨ࠰࡯ࡳ࡬࠭ᶂ"), bstack1lll11l_opy_ (u"ࠩࡤࠫᶃ")) as f:
            f.write(message + bstack1lll11l_opy_ (u"ࠪࡠࡳ࠭ᶄ"))
def bstack1lll11l1lll_opy_():
    return os.environ[bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧᶅ")].lower() == bstack1lll11l_opy_ (u"ࠬࡺࡲࡶࡧࠪᶆ")
def bstack1l111lll_opy_():
    return bstack11llll11_opy_().replace(tzinfo=None).isoformat() + bstack1lll11l_opy_ (u"࡚࠭ࠨᶇ")
def bstack111l1l1l11l_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack1lll11l_opy_ (u"࡛ࠧࠩᶈ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack1lll11l_opy_ (u"ࠨ࡜ࠪᶉ")))).total_seconds() * 1000
def bstack1111llllll1_opy_(timestamp):
    return bstack1111l1l1111_opy_(timestamp).isoformat() + bstack1lll11l_opy_ (u"ࠩ࡝ࠫᶊ")
def bstack111l11111l1_opy_(bstack1111l1lllll_opy_):
    date_format = bstack1lll11l_opy_ (u"ࠪࠩ࡞ࠫ࡭ࠦࡦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗ࠳ࠫࡦࠨᶋ")
    bstack1111l1lll1l_opy_ = datetime.datetime.strptime(bstack1111l1lllll_opy_, date_format)
    return bstack1111l1lll1l_opy_.isoformat() + bstack1lll11l_opy_ (u"ࠫ࡟࠭ᶌ")
def bstack111l1l1llll_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack1lll11l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᶍ")
    else:
        return bstack1lll11l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᶎ")
def bstack111llll1l_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack1lll11l_opy_ (u"ࠧࡵࡴࡸࡩࠬᶏ")
def bstack111l1111ll1_opy_(val):
    return val.__str__().lower() == bstack1lll11l_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧᶐ")
def error_handler(bstack1111l11ll1l_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1111l11ll1l_opy_ as e:
                print(bstack1lll11l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡿࢂࠦ࠭࠿ࠢࡾࢁ࠿ࠦࡻࡾࠤᶑ").format(func.__name__, bstack1111l11ll1l_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1111l1l1l1l_opy_(bstack111l1l11111_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack111l1l11111_opy_(cls, *args, **kwargs)
            except bstack1111l11ll1l_opy_ as e:
                print(bstack1lll11l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࢀࢃࠠ࠮ࡀࠣࡿࢂࡀࠠࡼࡿࠥᶒ").format(bstack111l1l11111_opy_.__name__, bstack1111l11ll1l_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1111l1l1l1l_opy_
    else:
        return decorator
def bstack11111lll1l_opy_(bstack1lll11l1l_opy_):
    if os.getenv(bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧᶓ")) is not None:
        return bstack111llll1l_opy_(os.getenv(bstack1lll11l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨᶔ")))
    if bstack1lll11l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᶕ") in bstack1lll11l1l_opy_ and bstack111l1111ll1_opy_(bstack1lll11l1l_opy_[bstack1lll11l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᶖ")]):
        return False
    if bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᶗ") in bstack1lll11l1l_opy_ and bstack111l1111ll1_opy_(bstack1lll11l1l_opy_[bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᶘ")]):
        return False
    return True
def bstack11llll111l_opy_():
    try:
        from pytest_bdd import reporting
        bstack1111l1ll111_opy_ = os.environ.get(bstack1lll11l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡘࡗࡊࡘ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠥᶙ"), None)
        return bstack1111l1ll111_opy_ is None or bstack1111l1ll111_opy_ == bstack1lll11l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣᶚ")
    except Exception as e:
        return False
def bstack11l11lll1l_opy_(hub_url, CONFIG):
    if bstack111l1l111l_opy_() <= version.parse(bstack1lll11l_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬᶛ")):
        if hub_url:
            return bstack1lll11l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢᶜ") + hub_url + bstack1lll11l_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦᶝ")
        return bstack11l1l111ll_opy_
    if hub_url:
        return bstack1lll11l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥᶞ") + hub_url + bstack1lll11l_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥᶟ")
    return bstack1ll1llllll_opy_
def bstack1111l11l1ll_opy_():
    return isinstance(os.getenv(bstack1lll11l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡐ࡚ࡍࡉࡏࠩᶠ")), str)
def bstack1111lllll1_opy_(url):
    return urlparse(url).hostname
def bstack1l1lll1111_opy_(hostname):
    for bstack111ll11l1l_opy_ in bstack1lllll1111_opy_:
        regex = re.compile(bstack111ll11l1l_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll111111l_opy_(bstack111l111ll11_opy_, file_name, logger):
    bstack111lll1ll1_opy_ = os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠫࢃ࠭ᶡ")), bstack111l111ll11_opy_)
    try:
        if not os.path.exists(bstack111lll1ll1_opy_):
            os.makedirs(bstack111lll1ll1_opy_)
        file_path = os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠬࢄࠧᶢ")), bstack111l111ll11_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack1lll11l_opy_ (u"࠭ࡷࠨᶣ")):
                pass
            with open(file_path, bstack1lll11l_opy_ (u"ࠢࡸ࠭ࠥᶤ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1lll1111ll_opy_.format(str(e)))
def bstack11l1llllll1_opy_(file_name, key, value, logger):
    file_path = bstack11ll111111l_opy_(bstack1lll11l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᶥ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack111l1ll111_opy_ = json.load(open(file_path, bstack1lll11l_opy_ (u"ࠩࡵࡦࠬᶦ")))
        else:
            bstack111l1ll111_opy_ = {}
        bstack111l1ll111_opy_[key] = value
        with open(file_path, bstack1lll11l_opy_ (u"ࠥࡻ࠰ࠨᶧ")) as outfile:
            json.dump(bstack111l1ll111_opy_, outfile)
def bstack11l111llll_opy_(file_name, logger):
    file_path = bstack11ll111111l_opy_(bstack1lll11l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᶨ"), file_name, logger)
    bstack111l1ll111_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack1lll11l_opy_ (u"ࠬࡸࠧᶩ")) as bstack111ll11lll_opy_:
            bstack111l1ll111_opy_ = json.load(bstack111ll11lll_opy_)
    return bstack111l1ll111_opy_
def bstack11l1l1ll11_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack1lll11l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡦࡨࡰࡪࡺࡩ࡯ࡩࠣࡪ࡮ࡲࡥ࠻ࠢࠪᶪ") + file_path + bstack1lll11l_opy_ (u"ࠧࠡࠩᶫ") + str(e))
def bstack111l1l111l_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack1lll11l_opy_ (u"ࠣ࠾ࡑࡓ࡙࡙ࡅࡕࡀࠥᶬ")
def bstack1l1ll1111_opy_(config):
    if bstack1lll11l_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᶭ") in config:
        del (config[bstack1lll11l_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᶮ")])
        return False
    if bstack111l1l111l_opy_() < version.parse(bstack1lll11l_opy_ (u"ࠫ࠸࠴࠴࠯࠲ࠪᶯ")):
        return False
    if bstack111l1l111l_opy_() >= version.parse(bstack1lll11l_opy_ (u"ࠬ࠺࠮࠲࠰࠸ࠫᶰ")):
        return True
    if bstack1lll11l_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ᶱ") in config and config[bstack1lll11l_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧᶲ")] is False:
        return False
    else:
        return True
def bstack11lll1ll11_opy_(args_list, bstack1111ll1l1ll_opy_):
    index = -1
    for value in bstack1111ll1l1ll_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack1111ll11l1l_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack1111ll11l1l_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack11lll11l_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack11lll11l_opy_ = bstack11lll11l_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack1lll11l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᶳ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack1lll11l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᶴ"), exception=exception)
    def bstack1111111lll_opy_(self):
        if self.result != bstack1lll11l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᶵ"):
            return None
        if isinstance(self.exception_type, str) and bstack1lll11l_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢᶶ") in self.exception_type:
            return bstack1lll11l_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨᶷ")
        return bstack1lll11l_opy_ (u"ࠨࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠢᶸ")
    def bstack1111lllll11_opy_(self):
        if self.result != bstack1lll11l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᶹ"):
            return None
        if self.bstack11lll11l_opy_:
            return self.bstack11lll11l_opy_
        return bstack1111l1l1ll1_opy_(self.exception)
def bstack1111l1l1ll1_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack1111l1111ll_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1ll111ll_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack111ll111l_opy_(config, logger):
    try:
        import playwright
        bstack111l11l11ll_opy_ = playwright.__file__
        bstack111l1ll111l_opy_ = os.path.split(bstack111l11l11ll_opy_)
        bstack1111l11l111_opy_ = bstack111l1ll111l_opy_[0] + bstack1lll11l_opy_ (u"ࠨ࠱ࡧࡶ࡮ࡼࡥࡳ࠱ࡳࡥࡨࡱࡡࡨࡧ࠲ࡰ࡮ࡨ࠯ࡤ࡮࡬࠳ࡨࡲࡩ࠯࡬ࡶࠫᶺ")
        os.environ[bstack1lll11l_opy_ (u"ࠩࡊࡐࡔࡈࡁࡍࡡࡄࡋࡊࡔࡔࡠࡊࡗࡘࡕࡥࡐࡓࡑ࡛࡝ࠬᶻ")] = bstack1l11l11lll_opy_(config)
        with open(bstack1111l11l111_opy_, bstack1lll11l_opy_ (u"ࠪࡶࠬᶼ")) as f:
            file_content = f.read()
            bstack1111l11l1l1_opy_ = bstack1lll11l_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠪᶽ")
            bstack1111ll1l11l_opy_ = file_content.find(bstack1111l11l1l1_opy_)
            if bstack1111ll1l11l_opy_ == -1:
              process = subprocess.Popen(bstack1lll11l_opy_ (u"ࠧࡴࡰ࡮ࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠤᶾ"), shell=True, cwd=bstack111l1ll111l_opy_[0])
              process.wait()
              bstack111l111ll1l_opy_ = bstack1lll11l_opy_ (u"࠭ࠢࡶࡵࡨࠤࡸࡺࡲࡪࡥࡷࠦࡀ࠭ᶿ")
              bstack111l1l1l1l1_opy_ = bstack1lll11l_opy_ (u"ࠢࠣࠤࠣࡠࠧࡻࡳࡦࠢࡶࡸࡷ࡯ࡣࡵ࡞ࠥ࠿ࠥࡩ࡯࡯ࡵࡷࠤࢀࠦࡢࡰࡱࡷࡷࡹࡸࡡࡱࠢࢀࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨࠨࡩ࡯ࡳࡧࡧ࡬࠮ࡣࡪࡩࡳࡺࠧࠪ࠽ࠣ࡭࡫ࠦࠨࡱࡴࡲࡧࡪࡹࡳ࠯ࡧࡱࡺ࠳ࡍࡌࡐࡄࡄࡐࡤࡇࡇࡆࡐࡗࡣࡍ࡚ࡔࡑࡡࡓࡖࡔ࡞࡙ࠪࠢࡥࡳࡴࡺࡳࡵࡴࡤࡴ࠭࠯࠻ࠡࠤࠥࠦ᷀")
              bstack1111l1ll1l1_opy_ = file_content.replace(bstack111l111ll1l_opy_, bstack111l1l1l1l1_opy_)
              with open(bstack1111l11l111_opy_, bstack1lll11l_opy_ (u"ࠨࡹࠪ᷁")) as f:
                f.write(bstack1111l1ll1l1_opy_)
    except Exception as e:
        logger.error(bstack1llllll11l_opy_.format(str(e)))
def bstack1l1lll111l_opy_():
  try:
    bstack1111l1l11l1_opy_ = os.path.join(tempfile.gettempdir(), bstack1lll11l_opy_ (u"ࠩࡲࡴࡹ࡯࡭ࡢ࡮ࡢ࡬ࡺࡨ࡟ࡶࡴ࡯࠲࡯ࡹ࡯࡯᷂ࠩ"))
    bstack1111l1l11ll_opy_ = []
    if os.path.exists(bstack1111l1l11l1_opy_):
      with open(bstack1111l1l11l1_opy_) as f:
        bstack1111l1l11ll_opy_ = json.load(f)
      os.remove(bstack1111l1l11l1_opy_)
    return bstack1111l1l11ll_opy_
  except:
    pass
  return []
def bstack1111l1l1ll_opy_(bstack1l111111l1_opy_):
  try:
    bstack1111l1l11ll_opy_ = []
    bstack1111l1l11l1_opy_ = os.path.join(tempfile.gettempdir(), bstack1lll11l_opy_ (u"ࠪࡳࡵࡺࡩ࡮ࡣ࡯ࡣ࡭ࡻࡢࡠࡷࡵࡰ࠳ࡰࡳࡰࡰࠪ᷃"))
    if os.path.exists(bstack1111l1l11l1_opy_):
      with open(bstack1111l1l11l1_opy_) as f:
        bstack1111l1l11ll_opy_ = json.load(f)
    bstack1111l1l11ll_opy_.append(bstack1l111111l1_opy_)
    with open(bstack1111l1l11l1_opy_, bstack1lll11l_opy_ (u"ࠫࡼ࠭᷄")) as f:
        json.dump(bstack1111l1l11ll_opy_, f)
  except:
    pass
def bstack1111l1l11_opy_(logger, bstack111l11ll1ll_opy_ = False):
  try:
    test_name = os.environ.get(bstack1lll11l_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨ᷅"), bstack1lll11l_opy_ (u"࠭ࠧ᷆"))
    if test_name == bstack1lll11l_opy_ (u"ࠧࠨ᷇"):
        test_name = threading.current_thread().__dict__.get(bstack1lll11l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡃࡦࡧࡣࡹ࡫ࡳࡵࡡࡱࡥࡲ࡫ࠧ᷈"), bstack1lll11l_opy_ (u"ࠩࠪ᷉"))
    bstack1111llll1ll_opy_ = bstack1lll11l_opy_ (u"ࠪ࠰᷊ࠥ࠭").join(threading.current_thread().bstackTestErrorMessages)
    if bstack111l11ll1ll_opy_:
        bstack11lll1l11_opy_ = os.environ.get(bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ᷋"), bstack1lll11l_opy_ (u"ࠬ࠶ࠧ᷌"))
        bstack111lll111l_opy_ = {bstack1lll11l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ᷍"): test_name, bstack1lll11l_opy_ (u"ࠧࡦࡴࡵࡳࡷ᷎࠭"): bstack1111llll1ll_opy_, bstack1lll11l_opy_ (u"ࠨ࡫ࡱࡨࡪࡾ᷏ࠧ"): bstack11lll1l11_opy_}
        bstack1111lll11ll_opy_ = []
        bstack111l111l1ll_opy_ = os.path.join(tempfile.gettempdir(), bstack1lll11l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡳࡴࡵࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨ᷐"))
        if os.path.exists(bstack111l111l1ll_opy_):
            with open(bstack111l111l1ll_opy_) as f:
                bstack1111lll11ll_opy_ = json.load(f)
        bstack1111lll11ll_opy_.append(bstack111lll111l_opy_)
        with open(bstack111l111l1ll_opy_, bstack1lll11l_opy_ (u"ࠪࡻࠬ᷑")) as f:
            json.dump(bstack1111lll11ll_opy_, f)
    else:
        bstack111lll111l_opy_ = {bstack1lll11l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ᷒"): test_name, bstack1lll11l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᷓ"): bstack1111llll1ll_opy_, bstack1lll11l_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᷔ"): str(multiprocessing.current_process().name)}
        if bstack1lll11l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷࠫᷕ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack111lll111l_opy_)
  except Exception as e:
      logger.warn(bstack1lll11l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡴࡾࡺࡥࡴࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧᷖ").format(e))
def bstack1l11l1l11_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1lll11l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠤࡳࡵࡴࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡻࡳࡪࡰࡪࠤࡧࡧࡳࡪࡥࠣࡪ࡮ࡲࡥࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࡷࠬᷗ"))
    try:
      bstack1111lll1l1l_opy_ = []
      bstack111lll111l_opy_ = {bstack1lll11l_opy_ (u"ࠪࡲࡦࡳࡥࠨᷘ"): test_name, bstack1lll11l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᷙ"): error_message, bstack1lll11l_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᷚ"): index}
      bstack1111l11l11l_opy_ = os.path.join(tempfile.gettempdir(), bstack1lll11l_opy_ (u"࠭ࡲࡰࡤࡲࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧᷛ"))
      if os.path.exists(bstack1111l11l11l_opy_):
          with open(bstack1111l11l11l_opy_) as f:
              bstack1111lll1l1l_opy_ = json.load(f)
      bstack1111lll1l1l_opy_.append(bstack111lll111l_opy_)
      with open(bstack1111l11l11l_opy_, bstack1lll11l_opy_ (u"ࠧࡸࠩᷜ")) as f:
          json.dump(bstack1111lll1l1l_opy_, f)
    except Exception as e:
      logger.warn(bstack1lll11l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡶࡴࡨ࡯ࡵࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧ࠺ࠡࡽࢀࠦᷝ").format(e))
    return
  bstack1111lll1l1l_opy_ = []
  bstack111lll111l_opy_ = {bstack1lll11l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᷞ"): test_name, bstack1lll11l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᷟ"): error_message, bstack1lll11l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᷠ"): index}
  bstack1111l11l11l_opy_ = os.path.join(tempfile.gettempdir(), bstack1lll11l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ᷡ"))
  lock_file = bstack1111l11l11l_opy_ + bstack1lll11l_opy_ (u"࠭࠮࡭ࡱࡦ࡯ࠬᷢ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1111l11l11l_opy_):
          with open(bstack1111l11l11l_opy_, bstack1lll11l_opy_ (u"ࠧࡳࠩᷣ")) as f:
              content = f.read().strip()
              if content:
                  bstack1111lll1l1l_opy_ = json.load(open(bstack1111l11l11l_opy_))
      bstack1111lll1l1l_opy_.append(bstack111lll111l_opy_)
      with open(bstack1111l11l11l_opy_, bstack1lll11l_opy_ (u"ࠨࡹࠪᷤ")) as f:
          json.dump(bstack1111lll1l1l_opy_, f)
  except Exception as e:
    logger.warn(bstack1lll11l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡷࡵࡢࡰࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡࠡࡹ࡬ࡸ࡭ࠦࡦࡪ࡮ࡨࠤࡱࡵࡣ࡬࡫ࡱ࡫࠿ࠦࡻࡾࠤᷥ").format(e))
def bstack111lll1l1_opy_(bstack11ll1lll11_opy_, name, logger):
  try:
    bstack111lll111l_opy_ = {bstack1lll11l_opy_ (u"ࠪࡲࡦࡳࡥࠨᷦ"): name, bstack1lll11l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᷧ"): bstack11ll1lll11_opy_, bstack1lll11l_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᷨ"): str(threading.current_thread()._name)}
    return bstack111lll111l_opy_
  except Exception as e:
    logger.warn(bstack1lll11l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡤࡨ࡬ࡦࡼࡥࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥᷩ").format(e))
  return
def bstack111l1l11l1l_opy_():
    return platform.system() == bstack1lll11l_opy_ (u"ࠧࡘ࡫ࡱࡨࡴࡽࡳࠨᷪ")
def bstack111l111l1l_opy_(bstack111l1l11l11_opy_, config, logger):
    bstack1111l1lll11_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack111l1l11l11_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack1lll11l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡬ࡵࡧࡵࠤࡨࡵ࡮ࡧ࡫ࡪࠤࡰ࡫ࡹࡴࠢࡥࡽࠥࡸࡥࡨࡧࡻࠤࡲࡧࡴࡤࡪ࠽ࠤࢀࢃࠢᷫ").format(e))
    return bstack1111l1lll11_opy_
def bstack11l1l1l1ll1_opy_(bstack111l111l11l_opy_, bstack111l11ll111_opy_):
    bstack1111lll1ll1_opy_ = version.parse(bstack111l111l11l_opy_)
    bstack111l11l1ll1_opy_ = version.parse(bstack111l11ll111_opy_)
    if bstack1111lll1ll1_opy_ > bstack111l11l1ll1_opy_:
        return 1
    elif bstack1111lll1ll1_opy_ < bstack111l11l1ll1_opy_:
        return -1
    else:
        return 0
def bstack11llll11_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack1111l1l1111_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack1111ll1l111_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack11111llll1_opy_(options, framework, config, bstack11llll1l1_opy_={}):
    if options is None:
        return
    if getattr(options, bstack1lll11l_opy_ (u"ࠩࡪࡩࡹ࠭ᷬ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1l11ll1l1_opy_ = caps.get(bstack1lll11l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᷭ"))
    bstack111l1l1l111_opy_ = True
    bstack11l1lll11l_opy_ = os.environ[bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᷮ")]
    bstack1l1111l1lll_opy_ = config.get(bstack1lll11l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᷯ"), False)
    if bstack1l1111l1lll_opy_:
        bstack1l11ll11lll_opy_ = config.get(bstack1lll11l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᷰ"), {})
        bstack1l11ll11lll_opy_[bstack1lll11l_opy_ (u"ࠧࡢࡷࡷ࡬࡙ࡵ࡫ࡦࡰࠪᷱ")] = os.getenv(bstack1lll11l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ᷲ"))
        bstack1111ll11ll1_opy_ = json.loads(os.getenv(bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪᷳ"), bstack1lll11l_opy_ (u"ࠪࡿࢂ࠭ᷴ"))).get(bstack1lll11l_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ᷵"))
    if bstack111l1111ll1_opy_(caps.get(bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡘ࠵ࡆࠫ᷶"))) or bstack111l1111ll1_opy_(caps.get(bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦࡡࡺ࠷ࡨ᷷࠭"))):
        bstack111l1l1l111_opy_ = False
    if bstack1l1ll1111_opy_({bstack1lll11l_opy_ (u"ࠢࡶࡵࡨ࡛࠸ࡉ᷸ࠢ"): bstack111l1l1l111_opy_}):
        bstack1l11ll1l1_opy_ = bstack1l11ll1l1_opy_ or {}
        bstack1l11ll1l1_opy_[bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍ᷹ࠪ")] = bstack1111ll1l111_opy_(framework)
        bstack1l11ll1l1_opy_[bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ᷺ࠫ")] = bstack1lll11l1lll_opy_()
        bstack1l11ll1l1_opy_[bstack1lll11l_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭᷻")] = bstack11l1lll11l_opy_
        bstack1l11ll1l1_opy_[bstack1lll11l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭᷼")] = bstack11llll1l1_opy_
        if bstack1l1111l1lll_opy_:
            bstack1l11ll1l1_opy_[bstack1lll11l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ᷽ࠬ")] = bstack1l1111l1lll_opy_
            bstack1l11ll1l1_opy_[bstack1lll11l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭᷾")] = bstack1l11ll11lll_opy_
            bstack1l11ll1l1_opy_[bstack1lll11l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹ᷿ࠧ")][bstack1lll11l_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩḀ")] = bstack1111ll11ll1_opy_
        if getattr(options, bstack1lll11l_opy_ (u"ࠩࡶࡩࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵࡻࠪḁ"), None):
            options.set_capability(bstack1lll11l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫḂ"), bstack1l11ll1l1_opy_)
        else:
            options[bstack1lll11l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬḃ")] = bstack1l11ll1l1_opy_
    else:
        if getattr(options, bstack1lll11l_opy_ (u"ࠬࡹࡥࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸࡾ࠭Ḅ"), None):
            options.set_capability(bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧḅ"), bstack1111ll1l111_opy_(framework))
            options.set_capability(bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨḆ"), bstack1lll11l1lll_opy_())
            options.set_capability(bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪḇ"), bstack11l1lll11l_opy_)
            options.set_capability(bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪḈ"), bstack11llll1l1_opy_)
            if bstack1l1111l1lll_opy_:
                options.set_capability(bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩḉ"), bstack1l1111l1lll_opy_)
                options.set_capability(bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪḊ"), bstack1l11ll11lll_opy_)
                options.set_capability(bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶ࠲ࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬḋ"), bstack1111ll11ll1_opy_)
        else:
            options[bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧḌ")] = bstack1111ll1l111_opy_(framework)
            options[bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨḍ")] = bstack1lll11l1lll_opy_()
            options[bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪḎ")] = bstack11l1lll11l_opy_
            options[bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪḏ")] = bstack11llll1l1_opy_
            if bstack1l1111l1lll_opy_:
                options[bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩḐ")] = bstack1l1111l1lll_opy_
                options[bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪḑ")] = bstack1l11ll11lll_opy_
                options[bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫḒ")][bstack1lll11l_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧḓ")] = bstack1111ll11ll1_opy_
    return options
def bstack1111l1ll1ll_opy_(ws_endpoint, framework):
    bstack11llll1l1_opy_ = bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"ࠢࡑࡎࡄ࡝࡜ࡘࡉࡈࡊࡗࡣࡕࡘࡏࡅࡗࡆࡘࡤࡓࡁࡑࠤḔ"))
    if ws_endpoint and len(ws_endpoint.split(bstack1lll11l_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧḕ"))) > 1:
        ws_url = ws_endpoint.split(bstack1lll11l_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨḖ"))[0]
        if bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ḗ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack1111l1111l1_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack1lll11l_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪḘ"))[1]))
            bstack1111l1111l1_opy_ = bstack1111l1111l1_opy_ or {}
            bstack11l1lll11l_opy_ = os.environ[bstack1lll11l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪḙ")]
            bstack1111l1111l1_opy_[bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧḚ")] = str(framework) + str(__version__)
            bstack1111l1111l1_opy_[bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨḛ")] = bstack1lll11l1lll_opy_()
            bstack1111l1111l1_opy_[bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪḜ")] = bstack11l1lll11l_opy_
            bstack1111l1111l1_opy_[bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪḝ")] = bstack11llll1l1_opy_
            ws_endpoint = ws_endpoint.split(bstack1lll11l_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩḞ"))[0] + bstack1lll11l_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪḟ") + urllib.parse.quote(json.dumps(bstack1111l1111l1_opy_))
    return ws_endpoint
def bstack111l11111_opy_():
    global bstack1ll111llll_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1ll111llll_opy_ = BrowserType.connect
    return bstack1ll111llll_opy_
def bstack1l11l111l_opy_(framework_name):
    global bstack1l11l11ll_opy_
    bstack1l11l11ll_opy_ = framework_name
    return framework_name
def bstack11ll1111l1_opy_(self, *args, **kwargs):
    global bstack1ll111llll_opy_
    try:
        global bstack1l11l11ll_opy_
        if bstack1lll11l_opy_ (u"ࠬࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵࠩḠ") in kwargs:
            kwargs[bstack1lll11l_opy_ (u"࠭ࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶࠪḡ")] = bstack1111l1ll1ll_opy_(
                kwargs.get(bstack1lll11l_opy_ (u"ࠧࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷࠫḢ"), None),
                bstack1l11l11ll_opy_
            )
    except Exception as e:
        logger.error(bstack1lll11l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪࡨࡲࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡖࡈࡐࠦࡣࡢࡲࡶ࠾ࠥࢁࡽࠣḣ").format(str(e)))
    return bstack1ll111llll_opy_(self, *args, **kwargs)
def bstack111l1111l1l_opy_(bstack111l11llll1_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1lll1lll11_opy_(bstack111l11llll1_opy_, bstack1lll11l_opy_ (u"ࠤࠥḤ"))
        if proxies and proxies.get(bstack1lll11l_opy_ (u"ࠥ࡬ࡹࡺࡰࡴࠤḥ")):
            parsed_url = urlparse(proxies.get(bstack1lll11l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵࠥḦ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack1lll11l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡌࡴࡹࡴࠨḧ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack1lll11l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡵࡲࡵࠩḨ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack1lll11l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡛ࡳࡦࡴࠪḩ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack1lll11l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡢࡵࡶࠫḪ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack11lll1l1l1_opy_(bstack111l11llll1_opy_):
    bstack1111l111lll_opy_ = {
        bstack11l11l1l11l_opy_[bstack111l11l1l11_opy_]: bstack111l11llll1_opy_[bstack111l11l1l11_opy_]
        for bstack111l11l1l11_opy_ in bstack111l11llll1_opy_
        if bstack111l11l1l11_opy_ in bstack11l11l1l11l_opy_
    }
    bstack1111l111lll_opy_[bstack1lll11l_opy_ (u"ࠤࡳࡶࡴࡾࡹࡔࡧࡷࡸ࡮ࡴࡧࡴࠤḫ")] = bstack111l1111l1l_opy_(bstack111l11llll1_opy_, bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"ࠥࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵࠥḬ")))
    bstack111l1111l11_opy_ = [element.lower() for element in bstack11l11l11l1l_opy_]
    bstack111l111lll1_opy_(bstack1111l111lll_opy_, bstack111l1111l11_opy_)
    return bstack1111l111lll_opy_
def bstack111l111lll1_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack1lll11l_opy_ (u"ࠦ࠯࠰ࠪࠫࠤḭ")
    for value in d.values():
        if isinstance(value, dict):
            bstack111l111lll1_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack111l111lll1_opy_(item, keys)
def bstack1ll1l111111_opy_():
    bstack1111l1ll11l_opy_ = [os.environ.get(bstack1lll11l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡏࡌࡆࡕࡢࡈࡎࡘࠢḮ")), os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠨࡾࠣḯ")), bstack1lll11l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧḰ")), os.path.join(bstack1lll11l_opy_ (u"ࠨ࠱ࡷࡱࡵ࠭ḱ"), bstack1lll11l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩḲ"))]
    for path in bstack1111l1ll11l_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack1lll11l_opy_ (u"ࠥࡊ࡮ࡲࡥࠡࠩࠥḳ") + str(path) + bstack1lll11l_opy_ (u"ࠦࠬࠦࡥࡹ࡫ࡶࡸࡸ࠴ࠢḴ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack1lll11l_opy_ (u"ࠧࡍࡩࡷ࡫ࡱ࡫ࠥࡶࡥࡳ࡯࡬ࡷࡸ࡯࡯࡯ࡵࠣࡪࡴࡸࠠࠨࠤḵ") + str(path) + bstack1lll11l_opy_ (u"ࠨࠧࠣḶ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack1lll11l_opy_ (u"ࠢࡇ࡫࡯ࡩࠥ࠭ࠢḷ") + str(path) + bstack1lll11l_opy_ (u"ࠣࠩࠣࡥࡱࡸࡥࡢࡦࡼࠤ࡭ࡧࡳࠡࡶ࡫ࡩࠥࡸࡥࡲࡷ࡬ࡶࡪࡪࠠࡱࡧࡵࡱ࡮ࡹࡳࡪࡱࡱࡷ࠳ࠨḸ"))
            else:
                logger.debug(bstack1lll11l_opy_ (u"ࠤࡆࡶࡪࡧࡴࡪࡰࡪࠤ࡫࡯࡬ࡦࠢࠪࠦḹ") + str(path) + bstack1lll11l_opy_ (u"ࠥࠫࠥࡽࡩࡵࡪࠣࡻࡷ࡯ࡴࡦࠢࡳࡩࡷࡳࡩࡴࡵ࡬ࡳࡳ࠴ࠢḺ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack1lll11l_opy_ (u"ࠦࡔࡶࡥࡳࡣࡷ࡭ࡴࡴࠠࡴࡷࡦࡧࡪ࡫ࡤࡦࡦࠣࡪࡴࡸࠠࠨࠤḻ") + str(path) + bstack1lll11l_opy_ (u"ࠧ࠭࠮ࠣḼ"))
            return path
        except Exception as e:
            logger.debug(bstack1lll11l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡵࡱࠢࡩ࡭ࡱ࡫ࠠࠨࡽࡳࡥࡹ࡮ࡽࠨ࠼ࠣࠦḽ") + str(e) + bstack1lll11l_opy_ (u"ࠢࠣḾ"))
    logger.debug(bstack1lll11l_opy_ (u"ࠣࡃ࡯ࡰࠥࡶࡡࡵࡪࡶࠤ࡫ࡧࡩ࡭ࡧࡧ࠲ࠧḿ"))
    return None
@measure(event_name=EVENTS.bstack11l11ll1lll_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
def bstack1l11llll1l1_opy_(binary_path, bstack1l1l1l1lll1_opy_, bs_config):
    logger.debug(bstack1lll11l_opy_ (u"ࠤࡆࡹࡷࡸࡥ࡯ࡶࠣࡇࡑࡏࠠࡑࡣࡷ࡬ࠥ࡬࡯ࡶࡰࡧ࠾ࠥࢁࡽࠣṀ").format(binary_path))
    bstack111l11lll1l_opy_ = bstack1lll11l_opy_ (u"ࠪࠫṁ")
    bstack111l1l1ll1l_opy_ = {
        bstack1lll11l_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩṂ"): __version__,
        bstack1lll11l_opy_ (u"ࠧࡵࡳࠣṃ"): platform.system(),
        bstack1lll11l_opy_ (u"ࠨ࡯ࡴࡡࡤࡶࡨ࡮ࠢṄ"): platform.machine(),
        bstack1lll11l_opy_ (u"ࠢࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧṅ"): bstack1lll11l_opy_ (u"ࠨ࠲ࠪṆ"),
        bstack1lll11l_opy_ (u"ࠤࡶࡨࡰࡥ࡬ࡢࡰࡪࡹࡦ࡭ࡥࠣṇ"): bstack1lll11l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪṈ")
    }
    bstack1111llll1l1_opy_(bstack111l1l1ll1l_opy_)
    try:
        if binary_path:
            if bstack111l1l11l1l_opy_():
                bstack111l1l1ll1l_opy_[bstack1lll11l_opy_ (u"ࠫࡨࡲࡩࡠࡸࡨࡶࡸ࡯࡯࡯ࠩṉ")] = subprocess.check_output([binary_path, bstack1lll11l_opy_ (u"ࠧࡼࡥࡳࡵ࡬ࡳࡳࠨṊ")]).strip().decode(bstack1lll11l_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬṋ"))
            else:
                bstack111l1l1ll1l_opy_[bstack1lll11l_opy_ (u"ࠧࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬṌ")] = subprocess.check_output([binary_path, bstack1lll11l_opy_ (u"ࠣࡸࡨࡶࡸ࡯࡯࡯ࠤṍ")], stderr=subprocess.DEVNULL).strip().decode(bstack1lll11l_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨṎ"))
        response = requests.request(
            bstack1lll11l_opy_ (u"ࠪࡋࡊ࡚ࠧṏ"),
            url=bstack11111lll11_opy_(bstack11l11ll1111_opy_),
            headers=None,
            auth=(bs_config[bstack1lll11l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭Ṑ")], bs_config[bstack1lll11l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨṑ")]),
            json=None,
            params=bstack111l1l1ll1l_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack1lll11l_opy_ (u"࠭ࡵࡳ࡮ࠪṒ") in data.keys() and bstack1lll11l_opy_ (u"ࠧࡶࡲࡧࡥࡹ࡫ࡤࡠࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ṓ") in data.keys():
            logger.debug(bstack1lll11l_opy_ (u"ࠣࡐࡨࡩࡩࠦࡴࡰࠢࡸࡴࡩࡧࡴࡦࠢࡥ࡭ࡳࡧࡲࡺ࠮ࠣࡧࡺࡸࡲࡦࡰࡷࠤࡧ࡯࡮ࡢࡴࡼࠤࡻ࡫ࡲࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠤṔ").format(bstack111l1l1ll1l_opy_[bstack1lll11l_opy_ (u"ࠩࡦࡰ࡮ࡥࡶࡦࡴࡶ࡭ࡴࡴࠧṕ")]))
            if bstack1lll11l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡘࡖࡑ࠭Ṗ") in os.environ:
                logger.debug(bstack1lll11l_opy_ (u"ࠦࡘࡱࡩࡱࡲ࡬ࡲ࡬ࠦࡢࡪࡰࡤࡶࡾࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡣࡶࠤࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢ࡙ࡗࡒࠠࡪࡵࠣࡷࡪࡺࠢṗ"))
                data[bstack1lll11l_opy_ (u"ࠬࡻࡲ࡭ࠩṘ")] = os.environ[bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤ࡛ࡒࡍࠩṙ")]
            bstack111l11lllll_opy_ = bstack111l11l11l1_opy_(data[bstack1lll11l_opy_ (u"ࠧࡶࡴ࡯ࠫṚ")], bstack1l1l1l1lll1_opy_)
            bstack111l11lll1l_opy_ = os.path.join(bstack1l1l1l1lll1_opy_, bstack111l11lllll_opy_)
            os.chmod(bstack111l11lll1l_opy_, 0o777) # bstack1111ll1ll1l_opy_ permission
            return bstack111l11lll1l_opy_
    except Exception as e:
        logger.debug(bstack1lll11l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡤࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡳ࡫ࡷࠡࡕࡇࡏࠥࢁࡽࠣṛ").format(e))
    return binary_path
def bstack1111llll1l1_opy_(bstack111l1l1ll1l_opy_):
    try:
        if bstack1lll11l_opy_ (u"ࠩ࡯࡭ࡳࡻࡸࠨṜ") not in bstack111l1l1ll1l_opy_[bstack1lll11l_opy_ (u"ࠪࡳࡸ࠭ṝ")].lower():
            return
        if os.path.exists(bstack1lll11l_opy_ (u"ࠦ࠴࡫ࡴࡤ࠱ࡲࡷ࠲ࡸࡥ࡭ࡧࡤࡷࡪࠨṞ")):
            with open(bstack1lll11l_opy_ (u"ࠧ࠵ࡥࡵࡥ࠲ࡳࡸ࠳ࡲࡦ࡮ࡨࡥࡸ࡫ࠢṟ"), bstack1lll11l_opy_ (u"ࠨࡲࠣṠ")) as f:
                bstack111l1111111_opy_ = {}
                for line in f:
                    if bstack1lll11l_opy_ (u"ࠢ࠾ࠤṡ") in line:
                        key, value = line.rstrip().split(bstack1lll11l_opy_ (u"ࠣ࠿ࠥṢ"), 1)
                        bstack111l1111111_opy_[key] = value.strip(bstack1lll11l_opy_ (u"ࠩࠥࡠࠬ࠭ṣ"))
                bstack111l1l1ll1l_opy_[bstack1lll11l_opy_ (u"ࠪࡨ࡮ࡹࡴࡳࡱࠪṤ")] = bstack111l1111111_opy_.get(bstack1lll11l_opy_ (u"ࠦࡎࡊࠢṥ"), bstack1lll11l_opy_ (u"ࠧࠨṦ"))
        elif os.path.exists(bstack1lll11l_opy_ (u"ࠨ࠯ࡦࡶࡦ࠳ࡦࡲࡰࡪࡰࡨ࠱ࡷ࡫࡬ࡦࡣࡶࡩࠧṧ")):
            bstack111l1l1ll1l_opy_[bstack1lll11l_opy_ (u"ࠧࡥ࡫ࡶࡸࡷࡵࠧṨ")] = bstack1lll11l_opy_ (u"ࠨࡣ࡯ࡴ࡮ࡴࡥࠨṩ")
    except Exception as e:
        logger.debug(bstack1lll11l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡭ࡥࡵࠢࡧ࡭ࡸࡺࡲࡰࠢࡲࡪࠥࡲࡩ࡯ࡷࡻࠦṪ") + e)
@measure(event_name=EVENTS.bstack11l11l1l111_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
def bstack111l11l11l1_opy_(bstack1111ll111l1_opy_, bstack1111lllllll_opy_):
    logger.debug(bstack1lll11l_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽࠥ࡬ࡲࡰ࡯࠽ࠤࠧṫ") + str(bstack1111ll111l1_opy_) + bstack1lll11l_opy_ (u"ࠦࠧṬ"))
    zip_path = os.path.join(bstack1111lllllll_opy_, bstack1lll11l_opy_ (u"ࠧࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࡡࡩ࡭ࡱ࡫࠮ࡻ࡫ࡳࠦṭ"))
    bstack111l11lllll_opy_ = bstack1lll11l_opy_ (u"࠭ࠧṮ")
    with requests.get(bstack1111ll111l1_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack1lll11l_opy_ (u"ࠢࡸࡤࠥṯ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack1lll11l_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࡤࡰࡹࡱࡰࡴࡧࡤࡦࡦࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺ࠰ࠥṰ"))
    with zipfile.ZipFile(zip_path, bstack1lll11l_opy_ (u"ࠩࡵࠫṱ")) as zip_ref:
        bstack111l11l1l1l_opy_ = zip_ref.namelist()
        if len(bstack111l11l1l1l_opy_) > 0:
            bstack111l11lllll_opy_ = bstack111l11l1l1l_opy_[0] # bstack1111l111l11_opy_ bstack11l11ll11l1_opy_ will be bstack111l1ll1l1l_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack1111lllllll_opy_)
        logger.debug(bstack1lll11l_opy_ (u"ࠥࡊ࡮ࡲࡥࡴࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡧࡻࡸࡷࡧࡣࡵࡧࡧࠤࡹࡵࠠࠨࠤṲ") + str(bstack1111lllllll_opy_) + bstack1lll11l_opy_ (u"ࠦࠬࠨṳ"))
    os.remove(zip_path)
    return bstack111l11lllll_opy_
def get_cli_dir():
    bstack1111lllll1l_opy_ = bstack1ll1l111111_opy_()
    if bstack1111lllll1l_opy_:
        bstack1l1l1l1lll1_opy_ = os.path.join(bstack1111lllll1l_opy_, bstack1lll11l_opy_ (u"ࠧࡩ࡬ࡪࠤṴ"))
        if not os.path.exists(bstack1l1l1l1lll1_opy_):
            os.makedirs(bstack1l1l1l1lll1_opy_, mode=0o777, exist_ok=True)
        return bstack1l1l1l1lll1_opy_
    else:
        raise FileNotFoundError(bstack1lll11l_opy_ (u"ࠨࡎࡰࠢࡺࡶ࡮ࡺࡡࡣ࡮ࡨࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧࠣࡪࡴࡸࠠࡵࡪࡨࠤࡘࡊࡋࠡࡤ࡬ࡲࡦࡸࡹ࠯ࠤṵ"))
def bstack1l1l1111ll1_opy_(bstack1l1l1l1lll1_opy_):
    bstack1lll11l_opy_ (u"ࠢࠣࠤࡊࡩࡹࠦࡴࡩࡧࠣࡴࡦࡺࡨࠡࡨࡲࡶࠥࡺࡨࡦࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽࠥ࡯࡮ࠡࡣࠣࡻࡷ࡯ࡴࡢࡤ࡯ࡩࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹ࠯ࠤࠥࠦṶ")
    bstack1111lll111l_opy_ = [
        os.path.join(bstack1l1l1l1lll1_opy_, f)
        for f in os.listdir(bstack1l1l1l1lll1_opy_)
        if os.path.isfile(os.path.join(bstack1l1l1l1lll1_opy_, f)) and f.startswith(bstack1lll11l_opy_ (u"ࠣࡤ࡬ࡲࡦࡸࡹ࠮ࠤṷ"))
    ]
    if len(bstack1111lll111l_opy_) > 0:
        return max(bstack1111lll111l_opy_, key=os.path.getmtime) # get bstack1111ll1111l_opy_ binary
    return bstack1lll11l_opy_ (u"ࠤࠥṸ")
def bstack111l1ll11ll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l111l1ll11_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l111l1ll11_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack11llll111_opy_(data, keys, default=None):
    bstack1lll11l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡗࡦ࡬ࡥ࡭ࡻࠣ࡫ࡪࡺࠠࡢࠢࡱࡩࡸࡺࡥࡥࠢࡹࡥࡱࡻࡥࠡࡨࡵࡳࡲࠦࡡࠡࡦ࡬ࡧࡹ࡯࡯࡯ࡣࡵࡽࠥࡵࡲࠡ࡮࡬ࡷࡹ࠴ࠊࠡࠢࠣࠤ࠿ࡶࡡࡳࡣࡰࠤࡩࡧࡴࡢ࠼ࠣࡘ࡭࡫ࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼࠤࡴࡸࠠ࡭࡫ࡶࡸࠥࡺ࡯ࠡࡶࡵࡥࡻ࡫ࡲࡴࡧ࠱ࠎࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡ࡭ࡨࡽࡸࡀࠠࡂࠢ࡯࡭ࡸࡺࠠࡰࡨࠣ࡯ࡪࡿࡳ࠰࡫ࡱࡨ࡮ࡩࡥࡴࠢࡵࡩࡵࡸࡥࡴࡧࡱࡸ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡶࡡࡵࡪ࠱ࠎࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡࡦࡨࡪࡦࡻ࡬ࡵ࠼࡚ࠣࡦࡲࡵࡦࠢࡷࡳࠥࡸࡥࡵࡷࡵࡲࠥ࡯ࡦࠡࡶ࡫ࡩࠥࡶࡡࡵࡪࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠲ࠏࠦࠠࠡࠢ࠽ࡶࡪࡺࡵࡳࡰ࠽ࠤ࡙࡮ࡥࠡࡸࡤࡰࡺ࡫ࠠࡢࡶࠣࡸ࡭࡫ࠠ࡯ࡧࡶࡸࡪࡪࠠࡱࡣࡷ࡬࠱ࠦ࡯ࡳࠢࡧࡩ࡫ࡧࡵ࡭ࡶࠣ࡭࡫ࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥ࠰ࠍࠤࠥࠦࠠࠣࠤࠥṹ")
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