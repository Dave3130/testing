# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
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
from bstack_utils.constants import (bstack1ll11l1lll_opy_, bstack1lll1111ll_opy_, bstack11l11l1lll_opy_,
                                    bstack11l1l11l1l1_opy_, bstack11l11ll1111_opy_, bstack11l11ll1ll1_opy_, bstack11l1l11l1ll_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1l11ll1l11_opy_, bstack11l1l1ll11_opy_
from bstack_utils.proxy import bstack1l1ll111ll_opy_, bstack1l11ll111l_opy_
from bstack_utils.constants import *
from bstack_utils import bstack11l1l11ll1_opy_
from bstack_utils.bstack11l1ll111_opy_ import bstack1l11lll1l1_opy_
from browserstack_sdk._version import __version__
bstack1lll11111_opy_ = Config.bstack1llll111l_opy_()
logger = bstack11l1l11ll1_opy_.get_logger(__name__, bstack11l1l11ll1_opy_.bstack1l1l11llll1_opy_())
def bstack111l1l1lll1_opy_(config):
    return config[bstack11l11ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᰉ")]
def bstack111l1l1ll1l_opy_(config):
    return config[bstack11l11ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᰊ")]
def bstack11l111111_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack111l1l1l1ll_opy_(obj):
    values = []
    bstack1111lll111l_opy_ = re.compile(bstack11l11ll_opy_ (u"ࡶࠧࡤࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢࡠࡩ࠱ࠤࠣᰋ"), re.I)
    for key in obj.keys():
        if bstack1111lll111l_opy_.match(key):
            values.append(obj[key])
    return values
def bstack111l11l1lll_opy_(config):
    tags = []
    tags.extend(bstack111l1l1l1ll_opy_(os.environ))
    tags.extend(bstack111l1l1l1ll_opy_(config))
    return tags
def bstack1111ll1111l_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111l11lll1l_opy_(bstack111l111l1l1_opy_):
    if not bstack111l111l1l1_opy_:
        return bstack11l11ll_opy_ (u"ࠬ࠭ᰌ")
    return bstack11l11ll_opy_ (u"ࠨࡻࡾࠢࠫࡿࢂ࠯ࠢᰍ").format(bstack111l111l1l1_opy_.name, bstack111l111l1l1_opy_.email)
def bstack1111l11lll1_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack1111l111l1l_opy_ = repo.common_dir
        info = {
            bstack11l11ll_opy_ (u"ࠢࡴࡪࡤࠦᰎ"): repo.head.commit.hexsha,
            bstack11l11ll_opy_ (u"ࠣࡵ࡫ࡳࡷࡺ࡟ࡴࡪࡤࠦᰏ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack11l11ll_opy_ (u"ࠤࡥࡶࡦࡴࡣࡩࠤᰐ"): repo.active_branch.name,
            bstack11l11ll_opy_ (u"ࠥࡸࡦ࡭ࠢᰑ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack11l11ll_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡸࡪࡸࠢᰒ"): bstack111l11lll1l_opy_(repo.head.commit.committer),
            bstack11l11ll_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡹ࡫ࡲࡠࡦࡤࡸࡪࠨᰓ"): repo.head.commit.committed_datetime.isoformat(),
            bstack11l11ll_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࠨᰔ"): bstack111l11lll1l_opy_(repo.head.commit.author),
            bstack11l11ll_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸ࡟ࡥࡣࡷࡩࠧᰕ"): repo.head.commit.authored_datetime.isoformat(),
            bstack11l11ll_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡠ࡯ࡨࡷࡸࡧࡧࡦࠤᰖ"): repo.head.commit.message,
            bstack11l11ll_opy_ (u"ࠤࡵࡳࡴࡺࠢᰗ"): repo.git.rev_parse(bstack11l11ll_opy_ (u"ࠥ࠱࠲ࡹࡨࡰࡹ࠰ࡸࡴࡶ࡬ࡦࡸࡨࡰࠧᰘ")),
            bstack11l11ll_opy_ (u"ࠦࡨࡵ࡭࡮ࡱࡱࡣ࡬࡯ࡴࡠࡦ࡬ࡶࠧᰙ"): bstack1111l111l1l_opy_,
            bstack11l11ll_opy_ (u"ࠧࡽ࡯ࡳ࡭ࡷࡶࡪ࡫࡟ࡨ࡫ࡷࡣࡩ࡯ࡲࠣᰚ"): subprocess.check_output([bstack11l11ll_opy_ (u"ࠨࡧࡪࡶࠥᰛ"), bstack11l11ll_opy_ (u"ࠢࡳࡧࡹ࠱ࡵࡧࡲࡴࡧࠥᰜ"), bstack11l11ll_opy_ (u"ࠣ࠯࠰࡫࡮ࡺ࠭ࡤࡱࡰࡱࡴࡴ࠭ࡥ࡫ࡵࠦᰝ")]).strip().decode(
                bstack11l11ll_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᰞ")),
            bstack11l11ll_opy_ (u"ࠥࡰࡦࡹࡴࡠࡶࡤ࡫ࠧᰟ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack11l11ll_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡷࡤࡹࡩ࡯ࡥࡨࡣࡱࡧࡳࡵࡡࡷࡥ࡬ࠨᰠ"): repo.git.rev_list(
                bstack11l11ll_opy_ (u"ࠧࢁࡽ࠯࠰ࡾࢁࠧᰡ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack111l11lll11_opy_ = []
        for remote in remotes:
            bstack1111l1ll111_opy_ = {
                bstack11l11ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᰢ"): remote.name,
                bstack11l11ll_opy_ (u"ࠢࡶࡴ࡯ࠦᰣ"): remote.url,
            }
            bstack111l11lll11_opy_.append(bstack1111l1ll111_opy_)
        bstack111l1ll1111_opy_ = {
            bstack11l11ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᰤ"): bstack11l11ll_opy_ (u"ࠤࡪ࡭ࡹࠨᰥ"),
            **info,
            bstack11l11ll_opy_ (u"ࠥࡶࡪࡳ࡯ࡵࡧࡶࠦᰦ"): bstack111l11lll11_opy_
        }
        bstack111l1ll1111_opy_ = bstack111l11ll1ll_opy_(bstack111l1ll1111_opy_)
        return bstack111l1ll1111_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack11l11ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡴࡶࡵ࡭ࡣࡷ࡭ࡳ࡭ࠠࡈ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢᰧ").format(err))
        return {}
def bstack11ll1ll111l_opy_(bstack1111lllll11_opy_=None):
    bstack11l11ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡍࡥࡵࠢࡪ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡵࡳࡩࡨ࡯ࡦࡪࡥࡤࡰࡱࡿࠠࡧࡱࡵࡱࡦࡺࡴࡦࡦࠣࡪࡴࡸࠠࡂࡋࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦࡵࡴࡧࠣࡧࡦࡹࡥࡴࠢࡩࡳࡷࠦࡥࡢࡥ࡫ࠤ࡫ࡵ࡬ࡥࡧࡵࠤ࡮ࡴࠠࡵࡪࡨࠤࡱ࡯ࡳࡵ࠰ࠍࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡧࡱ࡯ࡨࡪࡸࡳࠡࠪ࡯࡭ࡸࡺࠬࠡࡱࡳࡸ࡮ࡵ࡮ࡢ࡮ࠬ࠾ࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡎࡰࡰࡨ࠾ࠥࡓ࡯࡯ࡱ࠰ࡶࡪࡶ࡯ࠡࡣࡳࡴࡷࡵࡡࡤࡪ࠯ࠤࡺࡹࡥࡴࠢࡦࡹࡷࡸࡥ࡯ࡶࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾ࡛ࠦࡰࡵ࠱࡫ࡪࡺࡣࡸࡦࠫ࠭ࡢࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡅ࡮ࡲࡷࡽࠥࡲࡩࡴࡶࠣ࡟ࡢࡀࠠࡎࡷ࡯ࡸ࡮࠳ࡲࡦࡲࡲࠤࡦࡶࡰࡳࡱࡤࡧ࡭ࠦࡷࡪࡶ࡫ࠤࡳࡵࠠࡴࡱࡸࡶࡨ࡫ࡳࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡨࡨ࠱ࠦࡲࡦࡶࡸࡶࡳࡹࠠ࡜࡟ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡵࡧࡴࡩࡵ࠽ࠤࡒࡻ࡬ࡵ࡫࠰ࡶࡪࡶ࡯ࠡࡣࡳࡴࡷࡵࡡࡤࡪࠣࡻ࡮ࡺࡨࠡࡵࡳࡩࡨ࡯ࡦࡪࡥࠣࡪࡴࡲࡤࡦࡴࡶࠤࡹࡵࠠࡢࡰࡤࡰࡾࢀࡥࠋࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡮࡬ࡷࡹࡀࠠࡍ࡫ࡶࡸࠥࡵࡦࠡࡦ࡬ࡧࡹࡹࠬࠡࡧࡤࡧ࡭ࠦࡣࡰࡰࡷࡥ࡮ࡴࡩ࡯ࡩࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡩࡳࡷࠦࡡࠡࡨࡲࡰࡩ࡫ࡲ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᰨ")
    if bstack1111lllll11_opy_ is None:
        bstack1111lllll11_opy_ = [os.getcwd()]
    elif isinstance(bstack1111lllll11_opy_, list) and len(bstack1111lllll11_opy_) == 0:
        return []
    results = []
    for folder in bstack1111lllll11_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack11l11ll_opy_ (u"ࠨࡰࡳࡋࡧࠦᰩ"): bstack11l11ll_opy_ (u"ࠢࠣᰪ"),
                bstack11l11ll_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢᰫ"): [],
                bstack11l11ll_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡵࠥᰬ"): [],
                bstack11l11ll_opy_ (u"ࠥࡴࡷࡊࡡࡵࡧࠥᰭ"): bstack11l11ll_opy_ (u"ࠦࠧᰮ"),
                bstack11l11ll_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡒ࡫ࡳࡴࡣࡪࡩࡸࠨᰯ"): [],
                bstack11l11ll_opy_ (u"ࠨࡰࡳࡖ࡬ࡸࡱ࡫ࠢᰰ"): bstack11l11ll_opy_ (u"ࠢࠣᰱ"),
                bstack11l11ll_opy_ (u"ࠣࡲࡵࡈࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠣᰲ"): bstack11l11ll_opy_ (u"ࠤࠥᰳ"),
                bstack11l11ll_opy_ (u"ࠥࡴࡷࡘࡡࡸࡆ࡬ࡪ࡫ࠨᰴ"): bstack11l11ll_opy_ (u"ࠦࠧᰵ")
            }
            bstack1111l1l1l11_opy_ = repo.active_branch.name
            bstack111l1ll111l_opy_ = repo.head.commit
            result[bstack11l11ll_opy_ (u"ࠧࡶࡲࡊࡦࠥᰶ")] = bstack111l1ll111l_opy_.hexsha
            bstack111l11l11ll_opy_ = _111l111ll1l_opy_(repo)
            logger.debug(bstack11l11ll_opy_ (u"ࠨࡂࡢࡵࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤ࡫ࡵࡲࠡࡥࡲࡱࡵࡧࡲࡪࡵࡲࡲ࠿᰷ࠦࠢ") + str(bstack111l11l11ll_opy_) + bstack11l11ll_opy_ (u"ࠢࠣ᰸"))
            if bstack111l11l11ll_opy_:
                try:
                    bstack1111l1lll1l_opy_ = repo.git.diff(bstack11l11ll_opy_ (u"ࠣ࠯࠰ࡲࡦࡳࡥ࠮ࡱࡱࡰࡾࠨ᰹"), bstack11ll111l_opy_ (u"ࠤࡾࡦࡦࡹࡥࡠࡤࡵࡥࡳࡩࡨࡾ࠰࠱࠲ࢀࡩࡵࡳࡴࡨࡲࡹࡥࡢࡳࡣࡱࡧ࡭ࢃࠢ᰺")).split(bstack11l11ll_opy_ (u"ࠪࡠࡳ࠭᰻"))
                    logger.debug(bstack11l11ll_opy_ (u"ࠦࡈ࡮ࡡ࡯ࡩࡨࡨࠥ࡬ࡩ࡭ࡧࡶࠤࡧ࡫ࡴࡸࡧࡨࡲࠥࢁࡢࡢࡵࡨࡣࡧࡸࡡ࡯ࡥ࡫ࢁࠥࡧ࡮ࡥࠢࡾࡧࡺࡸࡲࡦࡰࡷࡣࡧࡸࡡ࡯ࡥ࡫ࢁ࠿ࠦࠢ᰼") + str(bstack1111l1lll1l_opy_) + bstack11l11ll_opy_ (u"ࠧࠨ᰽"))
                    result[bstack11l11ll_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧ᰾")] = [f.strip() for f in bstack1111l1lll1l_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack11ll111l_opy_ (u"ࠢࡼࡤࡤࡷࡪࡥࡢࡳࡣࡱࡧ࡭ࢃ࠮࠯ࡽࡦࡹࡷࡸࡥ࡯ࡶࡢࡦࡷࡧ࡮ࡤࡪࢀࠦ᰿")))
                except Exception:
                    logger.debug(bstack11l11ll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡬࡫ࡴࠡࡥ࡫ࡥࡳ࡭ࡥࡥࠢࡩ࡭ࡱ࡫ࡳࠡࡨࡵࡳࡲࠦࡢࡳࡣࡱࡧ࡭ࠦࡣࡰ࡯ࡳࡥࡷ࡯ࡳࡰࡰ࠱ࠤࡋࡧ࡬࡭࡫ࡱ࡫ࠥࡨࡡࡤ࡭ࠣࡸࡴࠦࡲࡦࡥࡨࡲࡹࠦࡣࡰ࡯ࡰ࡭ࡹࡹ࠮ࠣ᱀"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack11l11ll_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣ᱁")] = _1111l1l1lll_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack11l11ll_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤ᱂")] = _1111l1l1lll_opy_(commits[:5])
            bstack111l111lll1_opy_ = set()
            bstack111l1ll11l1_opy_ = []
            for commit in commits:
                logger.debug(bstack11l11ll_opy_ (u"ࠦࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡥࡲࡱࡲ࡯ࡴ࠻ࠢࠥ᱃") + str(commit.message) + bstack11l11ll_opy_ (u"ࠧࠨ᱄"))
                bstack1111l1lllll_opy_ = commit.author.name if commit.author else bstack11l11ll_opy_ (u"ࠨࡕ࡯࡭ࡱࡳࡼࡴࠢ᱅")
                bstack111l111lll1_opy_.add(bstack1111l1lllll_opy_)
                bstack111l1ll11l1_opy_.append({
                    bstack11l11ll_opy_ (u"ࠢ࡮ࡧࡶࡷࡦ࡭ࡥࠣ᱆"): commit.message.strip(),
                    bstack11l11ll_opy_ (u"ࠣࡷࡶࡩࡷࠨ᱇"): bstack1111l1lllll_opy_
                })
            result[bstack11l11ll_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡵࠥ᱈")] = list(bstack111l111lll1_opy_)
            result[bstack11l11ll_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡐࡩࡸࡹࡡࡨࡧࡶࠦ᱉")] = bstack111l1ll11l1_opy_
            result[bstack11l11ll_opy_ (u"ࠦࡵࡸࡄࡢࡶࡨࠦ᱊")] = bstack111l1ll111l_opy_.committed_datetime.strftime(bstack11l11ll_opy_ (u"࡙ࠧࠫ࠮ࠧࡰ࠱ࠪࡪࠢ᱋"))
            if (not result[bstack11l11ll_opy_ (u"ࠨࡰࡳࡖ࡬ࡸࡱ࡫ࠢ᱌")] or result[bstack11l11ll_opy_ (u"ࠢࡱࡴࡗ࡭ࡹࡲࡥࠣᱍ")].strip() == bstack11l11ll_opy_ (u"ࠣࠤᱎ")) and bstack111l1ll111l_opy_.message:
                bstack111l1l1l111_opy_ = bstack111l1ll111l_opy_.message.strip().splitlines()
                result[bstack11l11ll_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥᱏ")] = bstack111l1l1l111_opy_[0] if bstack111l1l1l111_opy_ else bstack11l11ll_opy_ (u"ࠥࠦ᱐")
                if len(bstack111l1l1l111_opy_) > 2:
                    result[bstack11l11ll_opy_ (u"ࠦࡵࡸࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠦ᱑")] = bstack11l11ll_opy_ (u"ࠬࡢ࡮ࠨ᱒").join(bstack111l1l1l111_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack11l11ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡯ࡱࡷ࡯ࡥࡹ࡯࡮ࡨࠢࡊ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡨࡲࡶࠥࡇࡉࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱࠤ࠭࡬࡯࡭ࡦࡨࡶ࠿ࠦࡻࡾࠫ࠽ࠤࢀࢃࠠ࠮ࠢࡾࢁࠧ᱓").format(
                folder,
                type(err).__name__,
                str(err)
            ))
    filtered_results = [
        result
        for result in results
        if _111l111l111_opy_(result)
    ]
    return filtered_results
def _111l111l111_opy_(result):
    bstack11l11ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡉࡧ࡯ࡴࡪࡸࠠࡵࡱࠣࡧ࡭࡫ࡣ࡬ࠢ࡬ࡪࠥࡧࠠࡨ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡲࡦࡵࡸࡰࡹࠦࡩࡴࠢࡹࡥࡱ࡯ࡤࠡࠪࡱࡳࡳ࠳ࡥ࡮ࡲࡷࡽࠥ࡬ࡩ࡭ࡧࡶࡇ࡭ࡧ࡮ࡨࡧࡧࠤࡦࡴࡤࠡࡣࡸࡸ࡭ࡵࡲࡴࠫ࠱ࠎࠥࠦࠠࠡࠤࠥࠦ᱔")
    return (
        isinstance(result.get(bstack11l11ll_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢ᱕"), None), list)
        and len(result[bstack11l11ll_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣ᱖")]) > 0
        and isinstance(result.get(bstack11l11ll_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡶࠦ᱗"), None), list)
        and len(result[bstack11l11ll_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡷࠧ᱘")]) > 0
    )
def _111l111ll1l_opy_(repo):
    bstack11l11ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤ࡚ࠥࡲࡺࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡶ࡫ࡩࠥࡨࡡࡴࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡪࡴࡸࠠࡵࡪࡨࠤ࡬࡯ࡶࡦࡰࠣࡶࡪࡶ࡯ࠡࡹ࡬ࡸ࡭ࡵࡵࡵࠢ࡫ࡥࡷࡪࡣࡰࡦࡨࡨࠥࡴࡡ࡮ࡧࡶࠤࡦࡴࡤࠡࡹࡲࡶࡰࠦࡷࡪࡶ࡫ࠤࡦࡲ࡬ࠡࡘࡆࡗࠥࡶࡲࡰࡸ࡬ࡨࡪࡸࡳ࠯ࠌࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹࠠࡵࡪࡨࠤࡩ࡫ࡦࡢࡷ࡯ࡸࠥࡨࡲࡢࡰࡦ࡬ࠥ࡯ࡦࠡࡲࡲࡷࡸ࡯ࡢ࡭ࡧ࠯ࠤࡪࡲࡳࡦࠢࡑࡳࡳ࡫࠮ࠋࠢࠣࠤࠥࠨࠢࠣ᱙")
    try:
        try:
            origin = repo.remotes.origin
            bstack1111ll11l1l_opy_ = origin.refs[bstack11l11ll_opy_ (u"࠭ࡈࡆࡃࡇࠫᱚ")]
            target = bstack1111ll11l1l_opy_.reference.name
            if target.startswith(bstack11l11ll_opy_ (u"ࠧࡰࡴ࡬࡫࡮ࡴ࠯ࠨᱛ")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack11l11ll_opy_ (u"ࠨࡱࡵ࡭࡬࡯࡮࠰ࠩᱜ")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _1111l1l1lll_opy_(commits):
    bstack11l11ll_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡊࡩࡹࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡤࡪࡤࡲ࡬࡫ࡤࠡࡨ࡬ࡰࡪࡹࠠࡧࡴࡲࡱࠥࡧࠠ࡭࡫ࡶࡸࠥࡵࡦࠡࡥࡲࡱࡲ࡯ࡴࡴ࠰ࠍࠤࠥࠦࠠࠣࠤࠥᱝ")
    bstack1111l1lll1l_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack111l11l1l11_opy_ in diff:
                        if bstack111l11l1l11_opy_.a_path:
                            bstack1111l1lll1l_opy_.add(bstack111l11l1l11_opy_.a_path)
                        if bstack111l11l1l11_opy_.b_path:
                            bstack1111l1lll1l_opy_.add(bstack111l11l1l11_opy_.b_path)
    except Exception:
        pass
    return list(bstack1111l1lll1l_opy_)
def bstack111l11ll1ll_opy_(bstack111l1ll1111_opy_):
    bstack111l1111l1l_opy_ = bstack1111ll1ll11_opy_(bstack111l1ll1111_opy_)
    if bstack111l1111l1l_opy_ and bstack111l1111l1l_opy_ > bstack11l1l11l1l1_opy_:
        bstack1111l1ll11l_opy_ = bstack111l1111l1l_opy_ - bstack11l1l11l1l1_opy_
        bstack111l11111l1_opy_ = bstack111l11l111l_opy_(bstack111l1ll1111_opy_[bstack11l11ll_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡢࡱࡪࡹࡳࡢࡩࡨࠦᱞ")], bstack1111l1ll11l_opy_)
        bstack111l1ll1111_opy_[bstack11l11ll_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧᱟ")] = bstack111l11111l1_opy_
        logger.info(bstack11l11ll_opy_ (u"࡚ࠧࡨࡦࠢࡦࡳࡲࡳࡩࡵࠢ࡫ࡥࡸࠦࡢࡦࡧࡱࠤࡹࡸࡵ࡯ࡥࡤࡸࡪࡪ࠮ࠡࡕ࡬ࡾࡪࠦ࡯ࡧࠢࡦࡳࡲࡳࡩࡵࠢࡤࡪࡹ࡫ࡲࠡࡶࡵࡹࡳࡩࡡࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡽࢀࠤࡐࡈࠢᱠ")
                    .format(bstack1111ll1ll11_opy_(bstack111l1ll1111_opy_) / 1024))
    return bstack111l1ll1111_opy_
def bstack1111ll1ll11_opy_(json_data):
    try:
        if json_data:
            bstack111l11ll111_opy_ = json.dumps(json_data)
            bstack111l1111111_opy_ = sys.getsizeof(bstack111l11ll111_opy_)
            return bstack111l1111111_opy_
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠨࡓࡰ࡯ࡨࡸ࡭࡯࡮ࡨࠢࡺࡩࡳࡺࠠࡸࡴࡲࡲ࡬ࠦࡷࡩ࡫࡯ࡩࠥࡩࡡ࡭ࡥࡸࡰࡦࡺࡩ࡯ࡩࠣࡷ࡮ࢀࡥࠡࡱࡩࠤࡏ࡙ࡏࡏࠢࡲࡦ࡯࡫ࡣࡵ࠼ࠣࡿࢂࠨᱡ").format(e))
    return -1
def bstack111l11l111l_opy_(field, bstack1111llll1l1_opy_):
    try:
        bstack1111llll1ll_opy_ = len(bytes(bstack11l11ll1111_opy_, bstack11l11ll_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᱢ")))
        bstack1111l1ll1ll_opy_ = bytes(field, bstack11l11ll_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᱣ"))
        bstack111l1l1l1l1_opy_ = len(bstack1111l1ll1ll_opy_)
        bstack1111l11l1l1_opy_ = ceil(bstack111l1l1l1l1_opy_ - bstack1111llll1l1_opy_ - bstack1111llll1ll_opy_)
        if bstack1111l11l1l1_opy_ > 0:
            bstack111l1l11l1l_opy_ = bstack1111l1ll1ll_opy_[:bstack1111l11l1l1_opy_].decode(bstack11l11ll_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᱤ"), errors=bstack11l11ll_opy_ (u"ࠪ࡭࡬ࡴ࡯ࡳࡧࠪᱥ")) + bstack11l11ll1111_opy_
            return bstack111l1l11l1l_opy_
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡷࡶࡺࡴࡣࡢࡶ࡬ࡲ࡬ࠦࡦࡪࡧ࡯ࡨ࠱ࠦ࡮ࡰࡶ࡫࡭ࡳ࡭ࠠࡸࡣࡶࠤࡹࡸࡵ࡯ࡥࡤࡸࡪࡪࠠࡩࡧࡵࡩ࠿ࠦࡻࡾࠤᱦ").format(e))
    return field
def bstack11l11l11l_opy_():
    env = os.environ
    if (bstack11l11ll_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡕࡓࡎࠥᱧ") in env and len(env[bstack11l11ll_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡖࡔࡏࠦᱨ")]) > 0) or (
            bstack11l11ll_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡊࡒࡑࡊࠨᱩ") in env and len(env[bstack11l11ll_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡋࡓࡒࡋࠢᱪ")]) > 0):
        return {
            bstack11l11ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᱫ"): bstack11l11ll_opy_ (u"ࠥࡎࡪࡴ࡫ࡪࡰࡶࠦᱬ"),
            bstack11l11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᱭ"): env.get(bstack11l11ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᱮ")),
            bstack11l11ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᱯ"): env.get(bstack11l11ll_opy_ (u"ࠢࡋࡑࡅࡣࡓࡇࡍࡆࠤᱰ")),
            bstack11l11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᱱ"): env.get(bstack11l11ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᱲ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠥࡇࡎࠨᱳ")) == bstack11l11ll_opy_ (u"ࠦࡹࡸࡵࡦࠤᱴ") and bstack11lll1l11_opy_(env.get(bstack11l11ll_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡈࡏࠢᱵ"))):
        return {
            bstack11l11ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᱶ"): bstack11l11ll_opy_ (u"ࠢࡄ࡫ࡵࡧࡱ࡫ࡃࡊࠤᱷ"),
            bstack11l11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᱸ"): env.get(bstack11l11ll_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᱹ")),
            bstack11l11ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᱺ"): env.get(bstack11l11ll_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡣࡏࡕࡂࠣᱻ")),
            bstack11l11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᱼ"): env.get(bstack11l11ll_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࠤᱽ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠢࡄࡋࠥ᱾")) == bstack11l11ll_opy_ (u"ࠣࡶࡵࡹࡪࠨ᱿") and bstack11lll1l11_opy_(env.get(bstack11l11ll_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࠤᲀ"))):
        return {
            bstack11l11ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᲁ"): bstack11l11ll_opy_ (u"࡙ࠦࡸࡡࡷ࡫ࡶࠤࡈࡏࠢᲂ"),
            bstack11l11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᲃ"): env.get(bstack11l11ll_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡂࡖࡋࡏࡈࡤ࡝ࡅࡃࡡࡘࡖࡑࠨᲄ")),
            bstack11l11ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᲅ"): env.get(bstack11l11ll_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᲆ")),
            bstack11l11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲇ"): env.get(bstack11l11ll_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᲈ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠦࡈࡏࠢᲉ")) == bstack11l11ll_opy_ (u"ࠧࡺࡲࡶࡧࠥᲊ") and env.get(bstack11l11ll_opy_ (u"ࠨࡃࡊࡡࡑࡅࡒࡋࠢ᲋")) == bstack11l11ll_opy_ (u"ࠢࡤࡱࡧࡩࡸ࡮ࡩࡱࠤ᲌"):
        return {
            bstack11l11ll_opy_ (u"ࠣࡰࡤࡱࡪࠨ᲍"): bstack11l11ll_opy_ (u"ࠤࡆࡳࡩ࡫ࡳࡩ࡫ࡳࠦ᲎"),
            bstack11l11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᲏"): None,
            bstack11l11ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲐ"): None,
            bstack11l11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᲑ"): None
        }
    if env.get(bstack11l11ll_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡅࡖࡆࡔࡃࡉࠤᲒ")) and env.get(bstack11l11ll_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡇࡔࡓࡍࡊࡖࠥᲓ")):
        return {
            bstack11l11ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᲔ"): bstack11l11ll_opy_ (u"ࠤࡅ࡭ࡹࡨࡵࡤ࡭ࡨࡸࠧᲕ"),
            bstack11l11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᲖ"): env.get(bstack11l11ll_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡈࡋࡗࡣࡍ࡚ࡔࡑࡡࡒࡖࡎࡍࡉࡏࠤᲗ")),
            bstack11l11ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᲘ"): None,
            bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᲙ"): env.get(bstack11l11ll_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᲚ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠣࡅࡌࠦᲛ")) == bstack11l11ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᲜ") and bstack11lll1l11_opy_(env.get(bstack11l11ll_opy_ (u"ࠥࡈࡗࡕࡎࡆࠤᲝ"))):
        return {
            bstack11l11ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲞ"): bstack11l11ll_opy_ (u"ࠧࡊࡲࡰࡰࡨࠦᲟ"),
            bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᲠ"): env.get(bstack11l11ll_opy_ (u"ࠢࡅࡔࡒࡒࡊࡥࡂࡖࡋࡏࡈࡤࡒࡉࡏࡍࠥᲡ")),
            bstack11l11ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲢ"): None,
            bstack11l11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲣ"): env.get(bstack11l11ll_opy_ (u"ࠥࡈࡗࡕࡎࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᲤ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠦࡈࡏࠢᲥ")) == bstack11l11ll_opy_ (u"ࠧࡺࡲࡶࡧࠥᲦ") and bstack11lll1l11_opy_(env.get(bstack11l11ll_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࠤᲧ"))):
        return {
            bstack11l11ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲨ"): bstack11l11ll_opy_ (u"ࠣࡕࡨࡱࡦࡶࡨࡰࡴࡨࠦᲩ"),
            bstack11l11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲪ"): env.get(bstack11l11ll_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡏࡓࡉࡄࡒࡎࡠࡁࡕࡋࡒࡒࡤ࡛ࡒࡍࠤᲫ")),
            bstack11l11ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲬ"): env.get(bstack11l11ll_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᲭ")),
            bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᲮ"): env.get(bstack11l11ll_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡎࡔࡈ࡟ࡊࡆࠥᲯ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠣࡅࡌࠦᲰ")) == bstack11l11ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᲱ") and bstack11lll1l11_opy_(env.get(bstack11l11ll_opy_ (u"ࠥࡋࡎ࡚ࡌࡂࡄࡢࡇࡎࠨᲲ"))):
        return {
            bstack11l11ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲳ"): bstack11l11ll_opy_ (u"ࠧࡍࡩࡵࡎࡤࡦࠧᲴ"),
            bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᲵ"): env.get(bstack11l11ll_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡖࡔࡏࠦᲶ")),
            bstack11l11ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲷ"): env.get(bstack11l11ll_opy_ (u"ࠤࡆࡍࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᲸ")),
            bstack11l11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᲹ"): env.get(bstack11l11ll_opy_ (u"ࠦࡈࡏ࡟ࡋࡑࡅࡣࡎࡊࠢᲺ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠧࡉࡉࠣ᲻")) == bstack11l11ll_opy_ (u"ࠨࡴࡳࡷࡨࠦ᲼") and bstack11lll1l11_opy_(env.get(bstack11l11ll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࠥᲽ"))):
        return {
            bstack11l11ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᲾ"): bstack11l11ll_opy_ (u"ࠤࡅࡹ࡮ࡲࡤ࡬࡫ࡷࡩࠧᲿ"),
            bstack11l11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᳀"): env.get(bstack11l11ll_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥ᳁")),
            bstack11l11ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᳂"): env.get(bstack11l11ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡏࡅࡇࡋࡌࠣ᳃")) or env.get(bstack11l11ll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤࡔࡁࡎࡇࠥ᳄")),
            bstack11l11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᳅"): env.get(bstack11l11ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦ᳆"))
        }
    if bstack11lll1l11_opy_(env.get(bstack11l11ll_opy_ (u"ࠥࡘࡋࡥࡂࡖࡋࡏࡈࠧ᳇"))):
        return {
            bstack11l11ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᳈"): bstack11l11ll_opy_ (u"ࠧ࡜ࡩࡴࡷࡤࡰ࡙ࠥࡴࡶࡦ࡬ࡳ࡚ࠥࡥࡢ࡯ࠣࡗࡪࡸࡶࡪࡥࡨࡷࠧ᳉"),
            bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᳊"): bstack11l11ll_opy_ (u"ࠢࡼࡿࡾࢁࠧ᳋").format(env.get(bstack11l11ll_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡌࡏࡖࡐࡇࡅ࡙ࡏࡏࡏࡕࡈࡖ࡛ࡋࡒࡖࡔࡌࠫ᳌")), env.get(bstack11l11ll_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡐࡓࡑࡍࡉࡈ࡚ࡉࡅࠩ᳍"))),
            bstack11l11ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᳎"): env.get(bstack11l11ll_opy_ (u"ࠦࡘ࡟ࡓࡕࡇࡐࡣࡉࡋࡆࡊࡐࡌࡘࡎࡕࡎࡊࡆࠥ᳏")),
            bstack11l11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᳐"): env.get(bstack11l11ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉࠨ᳑"))
        }
    if bstack11lll1l11_opy_(env.get(bstack11l11ll_opy_ (u"ࠢࡂࡒࡓ࡚ࡊ࡟ࡏࡓࠤ᳒"))):
        return {
            bstack11l11ll_opy_ (u"ࠣࡰࡤࡱࡪࠨ᳓"): bstack11l11ll_opy_ (u"ࠤࡄࡴࡵࡼࡥࡺࡱࡵ᳔ࠦ"),
            bstack11l11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᳕"): bstack11l11ll_opy_ (u"ࠦࢀࢃ࠯ࡱࡴࡲ࡮ࡪࡩࡴ࠰ࡽࢀ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ᳖ࠥ").format(env.get(bstack11l11ll_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡖࡔࡏ᳗ࠫ")), env.get(bstack11l11ll_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡃࡆࡇࡔ࡛ࡎࡕࡡࡑࡅࡒࡋ᳘ࠧ")), env.get(bstack11l11ll_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡓࡖࡔࡐࡅࡄࡖࡢࡗࡑ࡛ࡇࠨ᳙")), env.get(bstack11l11ll_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬ᳚"))),
            bstack11l11ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ᳛"): env.get(bstack11l11ll_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡐࡏࡃࡡࡑࡅࡒࡋ᳜ࠢ")),
            bstack11l11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴ᳝ࠥ"): env.get(bstack11l11ll_opy_ (u"ࠧࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨ᳞"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠨࡁ࡛ࡗࡕࡉࡤࡎࡔࡕࡒࡢ࡙ࡘࡋࡒࡠࡃࡊࡉࡓ࡚᳟ࠢ")) and env.get(bstack11l11ll_opy_ (u"ࠢࡕࡈࡢࡆ࡚ࡏࡌࡅࠤ᳠")):
        return {
            bstack11l11ll_opy_ (u"ࠣࡰࡤࡱࡪࠨ᳡"): bstack11l11ll_opy_ (u"ࠤࡄࡾࡺࡸࡥࠡࡅࡌ᳢ࠦ"),
            bstack11l11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᳣"): bstack11l11ll_opy_ (u"ࠦࢀࢃࡻࡾ࠱ࡢࡦࡺ࡯࡬ࡥ࠱ࡵࡩࡸࡻ࡬ࡵࡵࡂࡦࡺ࡯࡬ࡥࡋࡧࡁࢀࢃ᳤ࠢ").format(env.get(bstack11l11ll_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡉࡓ࡚ࡔࡄࡂࡖࡌࡓࡓ࡙ࡅࡓࡘࡈࡖ࡚ࡘࡉࠨ᳥")), env.get(bstack11l11ll_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡔࡗࡕࡊࡆࡅࡗ᳦ࠫ")), env.get(bstack11l11ll_opy_ (u"ࠧࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊ᳧ࠧ"))),
            bstack11l11ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧ᳨ࠥ"): env.get(bstack11l11ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤᳩ")),
            bstack11l11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᳪ"): env.get(bstack11l11ll_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠦᳫ"))
        }
    if any([env.get(bstack11l11ll_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᳬ")), env.get(bstack11l11ll_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡕࡉࡘࡕࡌࡗࡇࡇࡣࡘࡕࡕࡓࡅࡈࡣ࡛ࡋࡒࡔࡋࡒࡒ᳭ࠧ")), env.get(bstack11l11ll_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡗࡔ࡛ࡒࡄࡇࡢ࡚ࡊࡘࡓࡊࡑࡑࠦᳮ"))]):
        return {
            bstack11l11ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᳯ"): bstack11l11ll_opy_ (u"ࠤࡄ࡛ࡘࠦࡃࡰࡦࡨࡆࡺ࡯࡬ࡥࠤᳰ"),
            bstack11l11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᳱ"): env.get(bstack11l11ll_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡑࡗࡅࡐࡎࡉ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᳲ")),
            bstack11l11ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᳳ"): env.get(bstack11l11ll_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦ᳴")),
            bstack11l11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᳵ"): env.get(bstack11l11ll_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᳶ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡏࡷࡰࡦࡪࡸࠢ᳷")):
        return {
            bstack11l11ll_opy_ (u"ࠥࡲࡦࡳࡥࠣ᳸"): bstack11l11ll_opy_ (u"ࠦࡇࡧ࡭ࡣࡱࡲࠦ᳹"),
            bstack11l11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᳺ"): env.get(bstack11l11ll_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡗ࡫ࡳࡶ࡮ࡷࡷ࡚ࡸ࡬ࠣ᳻")),
            bstack11l11ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᳼"): env.get(bstack11l11ll_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡵ࡫ࡳࡷࡺࡊࡰࡤࡑࡥࡲ࡫ࠢ᳽")),
            bstack11l11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᳾"): env.get(bstack11l11ll_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡐࡸࡱࡧ࡫ࡲࠣ᳿"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࠧᴀ")) or env.get(bstack11l11ll_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡍࡂࡋࡑࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡓࡕࡃࡕࡘࡊࡊࠢᴁ")):
        return {
            bstack11l11ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᴂ"): bstack11l11ll_opy_ (u"ࠢࡘࡧࡵࡧࡰ࡫ࡲࠣᴃ"),
            bstack11l11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᴄ"): env.get(bstack11l11ll_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᴅ")),
            bstack11l11ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴆ"): bstack11l11ll_opy_ (u"ࠦࡒࡧࡩ࡯ࠢࡓ࡭ࡵ࡫࡬ࡪࡰࡨࠦᴇ") if env.get(bstack11l11ll_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡍࡂࡋࡑࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡓࡕࡃࡕࡘࡊࡊࠢᴈ")) else None,
            bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴉ"): env.get(bstack11l11ll_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡉࡌࡘࡤࡉࡏࡎࡏࡌࡘࠧᴊ"))
        }
    if any([env.get(bstack11l11ll_opy_ (u"ࠣࡉࡆࡔࡤࡖࡒࡐࡌࡈࡇ࡙ࠨᴋ")), env.get(bstack11l11ll_opy_ (u"ࠤࡊࡇࡑࡕࡕࡅࡡࡓࡖࡔࡐࡅࡄࡖࠥᴌ")), env.get(bstack11l11ll_opy_ (u"ࠥࡋࡔࡕࡇࡍࡇࡢࡇࡑࡕࡕࡅࡡࡓࡖࡔࡐࡅࡄࡖࠥᴍ"))]):
        return {
            bstack11l11ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᴎ"): bstack11l11ll_opy_ (u"ࠧࡍ࡯ࡰࡩ࡯ࡩࠥࡉ࡬ࡰࡷࡧࠦᴏ"),
            bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᴐ"): None,
            bstack11l11ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᴑ"): env.get(bstack11l11ll_opy_ (u"ࠣࡒࡕࡓࡏࡋࡃࡕࡡࡌࡈࠧᴒ")),
            bstack11l11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᴓ"): env.get(bstack11l11ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᴔ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋࠢᴕ")):
        return {
            bstack11l11ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴖ"): bstack11l11ll_opy_ (u"ࠨࡓࡩ࡫ࡳࡴࡦࡨ࡬ࡦࠤᴗ"),
            bstack11l11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴘ"): env.get(bstack11l11ll_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᴙ")),
            bstack11l11ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᴚ"): bstack11l11ll_opy_ (u"ࠥࡎࡴࡨࠠࠤࡽࢀࠦᴛ").format(env.get(bstack11l11ll_opy_ (u"ࠫࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡋࡑࡅࡣࡎࡊࠧᴜ"))) if env.get(bstack11l11ll_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࡠࡌࡒࡆࡤࡏࡄࠣᴝ")) else None,
            bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴞ"): env.get(bstack11l11ll_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᴟ"))
        }
    if bstack11lll1l11_opy_(env.get(bstack11l11ll_opy_ (u"ࠣࡐࡈࡘࡑࡏࡆ࡚ࠤᴠ"))):
        return {
            bstack11l11ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᴡ"): bstack11l11ll_opy_ (u"ࠥࡒࡪࡺ࡬ࡪࡨࡼࠦᴢ"),
            bstack11l11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴣ"): env.get(bstack11l11ll_opy_ (u"ࠧࡊࡅࡑࡎࡒ࡝ࡤ࡛ࡒࡍࠤᴤ")),
            bstack11l11ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴥ"): env.get(bstack11l11ll_opy_ (u"ࠢࡔࡋࡗࡉࡤࡔࡁࡎࡇࠥᴦ")),
            bstack11l11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴧ"): env.get(bstack11l11ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᴨ"))
        }
    if bstack11lll1l11_opy_(env.get(bstack11l11ll_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢࡅࡈ࡚ࡉࡐࡐࡖࠦᴩ"))):
        return {
            bstack11l11ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᴪ"): bstack11l11ll_opy_ (u"ࠧࡍࡩࡵࡊࡸࡦࠥࡇࡣࡵ࡫ࡲࡲࡸࠨᴫ"),
            bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᴬ"): bstack11l11ll_opy_ (u"ࠢࡼࡿ࠲ࡿࢂ࠵ࡡࡤࡶ࡬ࡳࡳࡹ࠯ࡳࡷࡱࡷ࠴ࢁࡽࠣᴭ").format(env.get(bstack11l11ll_opy_ (u"ࠨࡉࡌࡘࡍ࡛ࡂࡠࡕࡈࡖ࡛ࡋࡒࡠࡗࡕࡐࠬᴮ")), env.get(bstack11l11ll_opy_ (u"ࠩࡊࡍ࡙ࡎࡕࡃࡡࡕࡉࡕࡕࡓࡊࡖࡒࡖ࡞࠭ᴯ")), env.get(bstack11l11ll_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡖ࡚ࡔ࡟ࡊࡆࠪᴰ"))),
            bstack11l11ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴱ"): env.get(bstack11l11ll_opy_ (u"ࠧࡍࡉࡕࡊࡘࡆࡤ࡝ࡏࡓࡍࡉࡐࡔ࡝ࠢᴲ")),
            bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᴳ"): env.get(bstack11l11ll_opy_ (u"ࠢࡈࡋࡗࡌ࡚ࡈ࡟ࡓࡗࡑࡣࡎࡊࠢᴴ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠣࡅࡌࠦᴵ")) == bstack11l11ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᴶ") and env.get(bstack11l11ll_opy_ (u"࡚ࠥࡊࡘࡃࡆࡎࠥᴷ")) == bstack11l11ll_opy_ (u"ࠦ࠶ࠨᴸ"):
        return {
            bstack11l11ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴹ"): bstack11l11ll_opy_ (u"ࠨࡖࡦࡴࡦࡩࡱࠨᴺ"),
            bstack11l11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴻ"): bstack11l11ll_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࡽࢀࠦᴼ").format(env.get(bstack11l11ll_opy_ (u"࡙ࠩࡉࡗࡉࡅࡍࡡࡘࡖࡑ࠭ᴽ"))),
            bstack11l11ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴾ"): None,
            bstack11l11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᴿ"): None,
        }
    if env.get(bstack11l11ll_opy_ (u"࡚ࠧࡅࡂࡏࡆࡍ࡙࡟࡟ࡗࡇࡕࡗࡎࡕࡎࠣᵀ")):
        return {
            bstack11l11ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᵁ"): bstack11l11ll_opy_ (u"ࠢࡕࡧࡤࡱࡨ࡯ࡴࡺࠤᵂ"),
            bstack11l11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᵃ"): None,
            bstack11l11ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᵄ"): env.get(bstack11l11ll_opy_ (u"ࠥࡘࡊࡇࡍࡄࡋࡗ࡝ࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡎࡂࡏࡈࠦᵅ")),
            bstack11l11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᵆ"): env.get(bstack11l11ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᵇ"))
        }
    if any([env.get(bstack11l11ll_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࠤᵈ")), env.get(bstack11l11ll_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࡢ࡙ࡗࡒࠢᵉ")), env.get(bstack11l11ll_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࡣ࡚࡙ࡅࡓࡐࡄࡑࡊࠨᵊ")), env.get(bstack11l11ll_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡚ࡅࡂࡏࠥᵋ"))]):
        return {
            bstack11l11ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᵌ"): bstack11l11ll_opy_ (u"ࠦࡈࡵ࡮ࡤࡱࡸࡶࡸ࡫ࠢᵍ"),
            bstack11l11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᵎ"): None,
            bstack11l11ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᵏ"): env.get(bstack11l11ll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᵐ")) or None,
            bstack11l11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᵑ"): env.get(bstack11l11ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᵒ"), 0)
        }
    if env.get(bstack11l11ll_opy_ (u"ࠥࡋࡔࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᵓ")):
        return {
            bstack11l11ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᵔ"): bstack11l11ll_opy_ (u"ࠧࡍ࡯ࡄࡆࠥᵕ"),
            bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᵖ"): None,
            bstack11l11ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᵗ"): env.get(bstack11l11ll_opy_ (u"ࠣࡉࡒࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᵘ")),
            bstack11l11ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᵙ"): env.get(bstack11l11ll_opy_ (u"ࠥࡋࡔࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡅࡒ࡙ࡓ࡚ࡅࡓࠤᵚ"))
        }
    if env.get(bstack11l11ll_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤᵛ")):
        return {
            bstack11l11ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᵜ"): bstack11l11ll_opy_ (u"ࠨࡃࡰࡦࡨࡊࡷ࡫ࡳࡩࠤᵝ"),
            bstack11l11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᵞ"): env.get(bstack11l11ll_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᵟ")),
            bstack11l11ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᵠ"): env.get(bstack11l11ll_opy_ (u"ࠥࡇࡋࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡐࡄࡑࡊࠨᵡ")),
            bstack11l11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᵢ"): env.get(bstack11l11ll_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᵣ"))
        }
    return {bstack11l11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᵤ"): None}
def get_host_info():
    return {
        bstack11l11ll_opy_ (u"ࠢࡩࡱࡶࡸࡳࡧ࡭ࡦࠤᵥ"): platform.node(),
        bstack11l11ll_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠥᵦ"): platform.system(),
        bstack11l11ll_opy_ (u"ࠤࡷࡽࡵ࡫ࠢᵧ"): platform.machine(),
        bstack11l11ll_opy_ (u"ࠥࡺࡪࡸࡳࡪࡱࡱࠦᵨ"): platform.version(),
        bstack11l11ll_opy_ (u"ࠦࡦࡸࡣࡩࠤᵩ"): platform.architecture()[0]
    }
def bstack11lll11l1_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111l111llll_opy_():
    if bstack1lll11111_opy_.get_property(bstack11l11ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭ᵪ")):
        return bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᵫ")
    return bstack11l11ll_opy_ (u"ࠧࡶࡰ࡮ࡲࡴࡽ࡮ࡠࡩࡵ࡭ࡩ࠭ᵬ")
def bstack111l1l111ll_opy_(driver):
    info = {
        bstack11l11ll_opy_ (u"ࠨࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧᵭ"): driver.capabilities,
        bstack11l11ll_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩ࠭ᵮ"): driver.session_id,
        bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫᵯ"): driver.capabilities.get(bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩᵰ"), None),
        bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᵱ"): driver.capabilities.get(bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᵲ"), None),
        bstack11l11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᵳ"): driver.capabilities.get(bstack11l11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧᵴ"), None),
        bstack11l11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᵵ"):driver.capabilities.get(bstack11l11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᵶ"), None),
    }
    if bstack111l111llll_opy_() == bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᵷ"):
        if bstack1l1ll1l11_opy_():
            info[bstack11l11ll_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᵸ")] = bstack11l11ll_opy_ (u"࠭ࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᵹ")
        elif driver.capabilities.get(bstack11l11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᵺ"), {}).get(bstack11l11ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬᵻ"), False):
            info[bstack11l11ll_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࠪᵼ")] = bstack11l11ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧᵽ")
        else:
            info[bstack11l11ll_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬᵾ")] = bstack11l11ll_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᵿ")
    return info
def bstack1l1ll1l11_opy_():
    if bstack1lll11111_opy_.get_property(bstack11l11ll_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᶀ")):
        return True
    if bstack11lll1l11_opy_(os.environ.get(bstack11l11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨᶁ"), None)):
        return True
    return False
def bstack1l111lll1_opy_(bstack1111l1l11l1_opy_, url, data, config):
    headers = config.get(bstack11l11ll_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩᶂ"), None)
    proxies = bstack1l1ll111ll_opy_(config, url)
    auth = config.get(bstack11l11ll_opy_ (u"ࠩࡤࡹࡹ࡮ࠧᶃ"), None)
    response = requests.request(
            bstack1111l1l11l1_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1111llll11_opy_(bstack1l1l11ll11_opy_, size):
    bstack1l1l111l1_opy_ = []
    while len(bstack1l1l11ll11_opy_) > size:
        bstack11ll1111ll_opy_ = bstack1l1l11ll11_opy_[:size]
        bstack1l1l111l1_opy_.append(bstack11ll1111ll_opy_)
        bstack1l1l11ll11_opy_ = bstack1l1l11ll11_opy_[size:]
    bstack1l1l111l1_opy_.append(bstack1l1l11ll11_opy_)
    return bstack1l1l111l1_opy_
def bstack1111ll1ll1l_opy_(message, bstack111l1l11lll_opy_=False):
    os.write(1, bytes(message, bstack11l11ll_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᶄ")))
    os.write(1, bytes(bstack11l11ll_opy_ (u"ࠫࡡࡴࠧᶅ"), bstack11l11ll_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᶆ")))
    if bstack111l1l11lll_opy_:
        with open(bstack11l11ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࠳࡯࠲࠳ࡼ࠱ࠬᶇ") + os.environ[bstack11l11ll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭ᶈ")] + bstack11l11ll_opy_ (u"ࠨ࠰࡯ࡳ࡬࠭ᶉ"), bstack11l11ll_opy_ (u"ࠩࡤࠫᶊ")) as f:
            f.write(message + bstack11l11ll_opy_ (u"ࠪࡠࡳ࠭ᶋ"))
def bstack1lll1l11l11_opy_():
    return os.environ[bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧᶌ")].lower() == bstack11l11ll_opy_ (u"ࠬࡺࡲࡶࡧࠪᶍ")
def bstack1ll1ll1l_opy_():
    return bstack1l1lllll_opy_().replace(tzinfo=None).isoformat() + bstack11l11ll_opy_ (u"࡚࠭ࠨᶎ")
def bstack1111l1111ll_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack11l11ll_opy_ (u"࡛ࠧࠩᶏ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack11l11ll_opy_ (u"ࠨ࡜ࠪᶐ")))).total_seconds() * 1000
def bstack1111llll111_opy_(timestamp):
    return bstack111l1l11111_opy_(timestamp).isoformat() + bstack11l11ll_opy_ (u"ࠩ࡝ࠫᶑ")
def bstack1111ll111ll_opy_(bstack111l1l111l1_opy_):
    date_format = bstack11l11ll_opy_ (u"ࠪࠩ࡞ࠫ࡭ࠦࡦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗ࠳ࠫࡦࠨᶒ")
    bstack1111ll111l1_opy_ = datetime.datetime.strptime(bstack111l1l111l1_opy_, date_format)
    return bstack1111ll111l1_opy_.isoformat() + bstack11l11ll_opy_ (u"ࠫ࡟࠭ᶓ")
def bstack1111lll1l1l_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack11l11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᶔ")
    else:
        return bstack11l11ll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᶕ")
def bstack11lll1l11_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack11l11ll_opy_ (u"ࠧࡵࡴࡸࡩࠬᶖ")
def bstack1111ll1l11l_opy_(val):
    return val.__str__().lower() == bstack11l11ll_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧᶗ")
def error_handler(bstack111l111l1ll_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111l111l1ll_opy_ as e:
                print(bstack11l11ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡿࢂࠦ࠭࠿ࠢࡾࢁ࠿ࠦࡻࡾࠤᶘ").format(func.__name__, bstack111l111l1ll_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1111l1l111l_opy_(bstack1111l1l1l1l_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1111l1l1l1l_opy_(cls, *args, **kwargs)
            except bstack111l111l1ll_opy_ as e:
                print(bstack11l11ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࢀࢃࠠ࠮ࡀࠣࡿࢂࡀࠠࡼࡿࠥᶙ").format(bstack1111l1l1l1l_opy_.__name__, bstack111l111l1ll_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1111l1l111l_opy_
    else:
        return decorator
def bstack111ll11l1l_opy_(bstack1llllllll_opy_):
    if os.getenv(bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧᶚ")) is not None:
        return bstack11lll1l11_opy_(os.getenv(bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨᶛ")))
    if bstack11l11ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᶜ") in bstack1llllllll_opy_ and bstack1111ll1l11l_opy_(bstack1llllllll_opy_[bstack11l11ll_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᶝ")]):
        return False
    if bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᶞ") in bstack1llllllll_opy_ and bstack1111ll1l11l_opy_(bstack1llllllll_opy_[bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᶟ")]):
        return False
    return True
def bstack11ll1l1l1_opy_():
    try:
        from pytest_bdd import reporting
        bstack1111ll11ll1_opy_ = os.environ.get(bstack11l11ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡘࡗࡊࡘ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠥᶠ"), None)
        return bstack1111ll11ll1_opy_ is None or bstack1111ll11ll1_opy_ == bstack11l11ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣᶡ")
    except Exception as e:
        return False
def bstack1111l1111l_opy_(hub_url, CONFIG):
    if bstack11l11l111_opy_() <= version.parse(bstack11l11ll_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬᶢ")):
        if hub_url:
            return bstack11l11ll_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢᶣ") + hub_url + bstack11l11ll_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦᶤ")
        return bstack1lll1111ll_opy_
    if hub_url:
        return bstack11l11ll_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥᶥ") + hub_url + bstack11l11ll_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥᶦ")
    return bstack11l11l1lll_opy_
def bstack1111l1lll11_opy_():
    return isinstance(os.getenv(bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡐ࡚ࡍࡉࡏࠩᶧ")), str)
def bstack111l1l11l_opy_(url):
    return urlparse(url).hostname
def bstack1111lll11l_opy_(hostname):
    for bstack1l1lll1l1l_opy_ in bstack1ll11l1lll_opy_:
        regex = re.compile(bstack1l1lll1l1l_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll1111l11_opy_(bstack1111l1llll1_opy_, file_name, logger):
    bstack11111lll1_opy_ = os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"ࠫࢃ࠭ᶨ")), bstack1111l1llll1_opy_)
    try:
        if not os.path.exists(bstack11111lll1_opy_):
            os.makedirs(bstack11111lll1_opy_)
        file_path = os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"ࠬࢄࠧᶩ")), bstack1111l1llll1_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack11l11ll_opy_ (u"࠭ࡷࠨᶪ")):
                pass
            with open(file_path, bstack11l11ll_opy_ (u"ࠢࡸ࠭ࠥᶫ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1l11ll1l11_opy_.format(str(e)))
def bstack11ll11111ll_opy_(file_name, key, value, logger):
    file_path = bstack11ll1111l11_opy_(bstack11l11ll_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᶬ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1l1l111ll1_opy_ = json.load(open(file_path, bstack11l11ll_opy_ (u"ࠩࡵࡦࠬᶭ")))
        else:
            bstack1l1l111ll1_opy_ = {}
        bstack1l1l111ll1_opy_[key] = value
        with open(file_path, bstack11l11ll_opy_ (u"ࠥࡻ࠰ࠨᶮ")) as outfile:
            json.dump(bstack1l1l111ll1_opy_, outfile)
def bstack1l1ll1ll1_opy_(file_name, logger):
    file_path = bstack11ll1111l11_opy_(bstack11l11ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᶯ"), file_name, logger)
    bstack1l1l111ll1_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack11l11ll_opy_ (u"ࠬࡸࠧᶰ")) as bstack11111l1ll1_opy_:
            bstack1l1l111ll1_opy_ = json.load(bstack11111l1ll1_opy_)
    return bstack1l1l111ll1_opy_
def bstack11111l1111_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡦࡨࡰࡪࡺࡩ࡯ࡩࠣࡪ࡮ࡲࡥ࠻ࠢࠪᶱ") + file_path + bstack11l11ll_opy_ (u"ࠧࠡࠩᶲ") + str(e))
def bstack11l11l111_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack11l11ll_opy_ (u"ࠣ࠾ࡑࡓ࡙࡙ࡅࡕࡀࠥᶳ")
def bstack1lllll1ll1_opy_(config):
    if bstack11l11ll_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᶴ") in config:
        del (config[bstack11l11ll_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᶵ")])
        return False
    if bstack11l11l111_opy_() < version.parse(bstack11l11ll_opy_ (u"ࠫ࠸࠴࠴࠯࠲ࠪᶶ")):
        return False
    if bstack11l11l111_opy_() >= version.parse(bstack11l11ll_opy_ (u"ࠬ࠺࠮࠲࠰࠸ࠫᶷ")):
        return True
    if bstack11l11ll_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ᶸ") in config and config[bstack11l11ll_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧᶹ")] is False:
        return False
    else:
        return True
def bstack1111111lll_opy_(args_list, bstack1111ll11111_opy_):
    index = -1
    for value in bstack1111ll11111_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack1111l111l11_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack1111l111l11_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1llll1l1_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1llll1l1_opy_ = bstack1llll1l1_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack11l11ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᶺ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack11l11ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᶻ"), exception=exception)
    def bstack11111111ll_opy_(self):
        if self.result != bstack11l11ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᶼ"):
            return None
        if isinstance(self.exception_type, str) and bstack11l11ll_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢᶽ") in self.exception_type:
            return bstack11l11ll_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨᶾ")
        return bstack11l11ll_opy_ (u"ࠨࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠢᶿ")
    def bstack1111l111lll_opy_(self):
        if self.result != bstack11l11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ᷀"):
            return None
        if self.bstack1llll1l1_opy_:
            return self.bstack1llll1l1_opy_
        return bstack111l11l11l1_opy_(self.exception)
def bstack111l11l11l1_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111l111111l_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l11l111_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack111l11l11_opy_(config, logger):
    try:
        import playwright
        bstack1111l111ll1_opy_ = playwright.__file__
        bstack111l1ll1l11_opy_ = os.path.split(bstack1111l111ll1_opy_)
        bstack1111lll11ll_opy_ = bstack111l1ll1l11_opy_[0] + bstack11l11ll_opy_ (u"ࠨ࠱ࡧࡶ࡮ࡼࡥࡳ࠱ࡳࡥࡨࡱࡡࡨࡧ࠲ࡰ࡮ࡨ࠯ࡤ࡮࡬࠳ࡨࡲࡩ࠯࡬ࡶࠫ᷁")
        os.environ[bstack11l11ll_opy_ (u"ࠩࡊࡐࡔࡈࡁࡍࡡࡄࡋࡊࡔࡔࡠࡊࡗࡘࡕࡥࡐࡓࡑ࡛࡝᷂ࠬ")] = bstack1l11ll111l_opy_(config)
        with open(bstack1111lll11ll_opy_, bstack11l11ll_opy_ (u"ࠪࡶࠬ᷃")) as f:
            file_content = f.read()
            bstack111l1l1l11l_opy_ = bstack11l11ll_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠪ᷄")
            bstack1111llll11l_opy_ = file_content.find(bstack111l1l1l11l_opy_)
            if bstack1111llll11l_opy_ == -1:
              process = subprocess.Popen(bstack11l11ll_opy_ (u"ࠧࡴࡰ࡮ࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠤ᷅"), shell=True, cwd=bstack111l1ll1l11_opy_[0])
              process.wait()
              bstack111l1ll11ll_opy_ = bstack11l11ll_opy_ (u"࠭ࠢࡶࡵࡨࠤࡸࡺࡲࡪࡥࡷࠦࡀ࠭᷆")
              bstack111l1ll1ll1_opy_ = bstack11l11ll_opy_ (u"ࠢࠣࠤࠣࡠࠧࡻࡳࡦࠢࡶࡸࡷ࡯ࡣࡵ࡞ࠥ࠿ࠥࡩ࡯࡯ࡵࡷࠤࢀࠦࡢࡰࡱࡷࡷࡹࡸࡡࡱࠢࢀࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨࠨࡩ࡯ࡳࡧࡧ࡬࠮ࡣࡪࡩࡳࡺࠧࠪ࠽ࠣ࡭࡫ࠦࠨࡱࡴࡲࡧࡪࡹࡳ࠯ࡧࡱࡺ࠳ࡍࡌࡐࡄࡄࡐࡤࡇࡇࡆࡐࡗࡣࡍ࡚ࡔࡑࡡࡓࡖࡔ࡞࡙ࠪࠢࡥࡳࡴࡺࡳࡵࡴࡤࡴ࠭࠯࠻ࠡࠤࠥࠦ᷇")
              bstack1111lll1ll1_opy_ = file_content.replace(bstack111l1ll11ll_opy_, bstack111l1ll1ll1_opy_)
              with open(bstack1111lll11ll_opy_, bstack11l11ll_opy_ (u"ࠨࡹࠪ᷈")) as f:
                f.write(bstack1111lll1ll1_opy_)
    except Exception as e:
        logger.error(bstack11l1l1ll11_opy_.format(str(e)))
def bstack1lllll1l11_opy_():
  try:
    bstack1111lll11l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11ll_opy_ (u"ࠩࡲࡴࡹ࡯࡭ࡢ࡮ࡢ࡬ࡺࡨ࡟ࡶࡴ࡯࠲࡯ࡹ࡯࡯ࠩ᷉"))
    bstack1111l1l1ll1_opy_ = []
    if os.path.exists(bstack1111lll11l1_opy_):
      with open(bstack1111lll11l1_opy_) as f:
        bstack1111l1l1ll1_opy_ = json.load(f)
      os.remove(bstack1111lll11l1_opy_)
    return bstack1111l1l1ll1_opy_
  except:
    pass
  return []
def bstack11l1111ll_opy_(bstack1ll1ll1l1_opy_):
  try:
    bstack1111l1l1ll1_opy_ = []
    bstack1111lll11l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11ll_opy_ (u"ࠪࡳࡵࡺࡩ࡮ࡣ࡯ࡣ࡭ࡻࡢࡠࡷࡵࡰ࠳ࡰࡳࡰࡰ᷊ࠪ"))
    if os.path.exists(bstack1111lll11l1_opy_):
      with open(bstack1111lll11l1_opy_) as f:
        bstack1111l1l1ll1_opy_ = json.load(f)
    bstack1111l1l1ll1_opy_.append(bstack1ll1ll1l1_opy_)
    with open(bstack1111lll11l1_opy_, bstack11l11ll_opy_ (u"ࠫࡼ࠭᷋")) as f:
        json.dump(bstack1111l1l1ll1_opy_, f)
  except:
    pass
def bstack1l1ll1l1l_opy_(logger, bstack111l111ll11_opy_ = False):
  try:
    test_name = os.environ.get(bstack11l11ll_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨ᷌"), bstack11l11ll_opy_ (u"࠭ࠧ᷍"))
    if test_name == bstack11l11ll_opy_ (u"ࠧࠨ᷎"):
        test_name = threading.current_thread().__dict__.get(bstack11l11ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡃࡦࡧࡣࡹ࡫ࡳࡵࡡࡱࡥࡲ࡫᷏ࠧ"), bstack11l11ll_opy_ (u"᷐ࠩࠪ"))
    bstack111l11ll11l_opy_ = bstack11l11ll_opy_ (u"ࠪ࠰ࠥ࠭᷑").join(threading.current_thread().bstackTestErrorMessages)
    if bstack111l111ll11_opy_:
        bstack11lll1ll11_opy_ = os.environ.get(bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ᷒"), bstack11l11ll_opy_ (u"ࠬ࠶ࠧᷓ"))
        bstack11lll1l1l1_opy_ = {bstack11l11ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᷔ"): test_name, bstack11l11ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᷕ"): bstack111l11ll11l_opy_, bstack11l11ll_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧᷖ"): bstack11lll1ll11_opy_}
        bstack1111l1l11ll_opy_ = []
        bstack111l11111ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡳࡴࡵࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨᷗ"))
        if os.path.exists(bstack111l11111ll_opy_):
            with open(bstack111l11111ll_opy_) as f:
                bstack1111l1l11ll_opy_ = json.load(f)
        bstack1111l1l11ll_opy_.append(bstack11lll1l1l1_opy_)
        with open(bstack111l11111ll_opy_, bstack11l11ll_opy_ (u"ࠪࡻࠬᷘ")) as f:
            json.dump(bstack1111l1l11ll_opy_, f)
    else:
        bstack11lll1l1l1_opy_ = {bstack11l11ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᷙ"): test_name, bstack11l11ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᷚ"): bstack111l11ll11l_opy_, bstack11l11ll_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᷛ"): str(multiprocessing.current_process().name)}
        if bstack11l11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷࠫᷜ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack11lll1l1l1_opy_)
  except Exception as e:
      logger.warn(bstack11l11ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡴࡾࡺࡥࡴࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧᷝ").format(e))
def bstack1l111l1ll_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l11ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠤࡳࡵࡴࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡻࡳࡪࡰࡪࠤࡧࡧࡳࡪࡥࠣࡪ࡮ࡲࡥࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࡷࠬᷞ"))
    try:
      bstack1111l11l1ll_opy_ = []
      bstack11lll1l1l1_opy_ = {bstack11l11ll_opy_ (u"ࠪࡲࡦࡳࡥࠨᷟ"): test_name, bstack11l11ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᷠ"): error_message, bstack11l11ll_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᷡ"): index}
      bstack1111llllll1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧᷢ"))
      if os.path.exists(bstack1111llllll1_opy_):
          with open(bstack1111llllll1_opy_) as f:
              bstack1111l11l1ll_opy_ = json.load(f)
      bstack1111l11l1ll_opy_.append(bstack11lll1l1l1_opy_)
      with open(bstack1111llllll1_opy_, bstack11l11ll_opy_ (u"ࠧࡸࠩᷣ")) as f:
          json.dump(bstack1111l11l1ll_opy_, f)
    except Exception as e:
      logger.warn(bstack11l11ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡶࡴࡨ࡯ࡵࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧ࠺ࠡࡽࢀࠦᷤ").format(e))
    return
  bstack1111l11l1ll_opy_ = []
  bstack11lll1l1l1_opy_ = {bstack11l11ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᷥ"): test_name, bstack11l11ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᷦ"): error_message, bstack11l11ll_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᷧ"): index}
  bstack1111llllll1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ᷨ"))
  lock_file = bstack1111llllll1_opy_ + bstack11l11ll_opy_ (u"࠭࠮࡭ࡱࡦ࡯ࠬᷩ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1111llllll1_opy_):
          with open(bstack1111llllll1_opy_, bstack11l11ll_opy_ (u"ࠧࡳࠩᷪ")) as f:
              content = f.read().strip()
              if content:
                  bstack1111l11l1ll_opy_ = json.load(open(bstack1111llllll1_opy_))
      bstack1111l11l1ll_opy_.append(bstack11lll1l1l1_opy_)
      with open(bstack1111llllll1_opy_, bstack11l11ll_opy_ (u"ࠨࡹࠪᷫ")) as f:
          json.dump(bstack1111l11l1ll_opy_, f)
  except Exception as e:
    logger.warn(bstack11l11ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡷࡵࡢࡰࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡࠡࡹ࡬ࡸ࡭ࠦࡦࡪ࡮ࡨࠤࡱࡵࡣ࡬࡫ࡱ࡫࠿ࠦࡻࡾࠤᷬ").format(e))
def bstack11l111ll1l_opy_(bstack1l1lll1ll1_opy_, name, logger):
  try:
    bstack11lll1l1l1_opy_ = {bstack11l11ll_opy_ (u"ࠪࡲࡦࡳࡥࠨᷭ"): name, bstack11l11ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᷮ"): bstack1l1lll1ll1_opy_, bstack11l11ll_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᷯ"): str(threading.current_thread()._name)}
    return bstack11lll1l1l1_opy_
  except Exception as e:
    logger.warn(bstack11l11ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡤࡨ࡬ࡦࡼࡥࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥᷰ").format(e))
  return
def bstack111l1l1111l_opy_():
    return platform.system() == bstack11l11ll_opy_ (u"ࠧࡘ࡫ࡱࡨࡴࡽࡳࠨᷱ")
def bstack1l111l111l_opy_(bstack1111ll1llll_opy_, config, logger):
    bstack1111l11ll1l_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack1111ll1llll_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡬ࡵࡧࡵࠤࡨࡵ࡮ࡧ࡫ࡪࠤࡰ࡫ࡹࡴࠢࡥࡽࠥࡸࡥࡨࡧࡻࠤࡲࡧࡴࡤࡪ࠽ࠤࢀࢃࠢᷲ").format(e))
    return bstack1111l11ll1l_opy_
def bstack11l1ll11111_opy_(bstack111l1111l11_opy_, bstack1111l11ll11_opy_):
    bstack111l1111ll1_opy_ = version.parse(bstack111l1111l11_opy_)
    bstack111l1ll1l1l_opy_ = version.parse(bstack1111l11ll11_opy_)
    if bstack111l1111ll1_opy_ > bstack111l1ll1l1l_opy_:
        return 1
    elif bstack111l1111ll1_opy_ < bstack111l1ll1l1l_opy_:
        return -1
    else:
        return 0
def bstack1l1lllll_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack111l1l11111_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack1111ll1l1ll_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1llll11ll1_opy_(options, framework, config, bstack11111l11l_opy_={}):
    if options is None:
        return
    if getattr(options, bstack11l11ll_opy_ (u"ࠩࡪࡩࡹ࠭ᷳ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1111l1l11l_opy_ = caps.get(bstack11l11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᷴ"))
    bstack111l111l11l_opy_ = True
    bstack1lll1111l1_opy_ = os.environ[bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ᷵")]
    bstack1l111l1ll1l_opy_ = config.get(bstack11l11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ᷶"), False)
    if bstack1l111l1ll1l_opy_:
        bstack1l1l1l1ll11_opy_ = config.get(bstack11l11ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ᷷࠭"), {})
        bstack1l1l1l1ll11_opy_[bstack11l11ll_opy_ (u"ࠧࡢࡷࡷ࡬࡙ࡵ࡫ࡦࡰ᷸ࠪ")] = os.getenv(bstack11l11ll_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙᷹࠭"))
        bstack1111ll1l1l1_opy_ = json.loads(os.getenv(bstack11l11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎ᷺ࠪ"), bstack11l11ll_opy_ (u"ࠪࡿࢂ࠭᷻"))).get(bstack11l11ll_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ᷼"))
    if bstack1111ll1l11l_opy_(caps.get(bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡘ࠵ࡆ᷽ࠫ"))) or bstack1111ll1l11l_opy_(caps.get(bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦࡡࡺ࠷ࡨ࠭᷾"))):
        bstack111l111l11l_opy_ = False
    if bstack1lllll1ll1_opy_({bstack11l11ll_opy_ (u"ࠢࡶࡵࡨ࡛࠸ࡉ᷿ࠢ"): bstack111l111l11l_opy_}):
        bstack1111l1l11l_opy_ = bstack1111l1l11l_opy_ or {}
        bstack1111l1l11l_opy_[bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪḀ")] = bstack1111ll1l1ll_opy_(framework)
        bstack1111l1l11l_opy_[bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫḁ")] = bstack1lll1l11l11_opy_()
        bstack1111l1l11l_opy_[bstack11l11ll_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭Ḃ")] = bstack1lll1111l1_opy_
        bstack1111l1l11l_opy_[bstack11l11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ḃ")] = bstack11111l11l_opy_
        if bstack1l111l1ll1l_opy_:
            bstack1111l1l11l_opy_[bstack11l11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬḄ")] = bstack1l111l1ll1l_opy_
            bstack1111l1l11l_opy_[bstack11l11ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ḅ")] = bstack1l1l1l1ll11_opy_
            bstack1111l1l11l_opy_[bstack11l11ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧḆ")][bstack11l11ll_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩḇ")] = bstack1111ll1l1l1_opy_
        if getattr(options, bstack11l11ll_opy_ (u"ࠩࡶࡩࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵࡻࠪḈ"), None):
            options.set_capability(bstack11l11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫḉ"), bstack1111l1l11l_opy_)
        else:
            options[bstack11l11ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬḊ")] = bstack1111l1l11l_opy_
    else:
        if getattr(options, bstack11l11ll_opy_ (u"ࠬࡹࡥࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸࡾ࠭ḋ"), None):
            options.set_capability(bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧḌ"), bstack1111ll1l1ll_opy_(framework))
            options.set_capability(bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨḍ"), bstack1lll1l11l11_opy_())
            options.set_capability(bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪḎ"), bstack1lll1111l1_opy_)
            options.set_capability(bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪḏ"), bstack11111l11l_opy_)
            if bstack1l111l1ll1l_opy_:
                options.set_capability(bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩḐ"), bstack1l111l1ll1l_opy_)
                options.set_capability(bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪḑ"), bstack1l1l1l1ll11_opy_)
                options.set_capability(bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶ࠲ࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬḒ"), bstack1111ll1l1l1_opy_)
        else:
            options[bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧḓ")] = bstack1111ll1l1ll_opy_(framework)
            options[bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨḔ")] = bstack1lll1l11l11_opy_()
            options[bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪḕ")] = bstack1lll1111l1_opy_
            options[bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪḖ")] = bstack11111l11l_opy_
            if bstack1l111l1ll1l_opy_:
                options[bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩḗ")] = bstack1l111l1ll1l_opy_
                options[bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪḘ")] = bstack1l1l1l1ll11_opy_
                options[bstack11l11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫḙ")][bstack11l11ll_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧḚ")] = bstack1111ll1l1l1_opy_
    return options
def bstack1111lll1111_opy_(ws_endpoint, framework):
    bstack11111l11l_opy_ = bstack1lll11111_opy_.get_property(bstack11l11ll_opy_ (u"ࠢࡑࡎࡄ࡝࡜ࡘࡉࡈࡊࡗࡣࡕࡘࡏࡅࡗࡆࡘࡤࡓࡁࡑࠤḛ"))
    if ws_endpoint and len(ws_endpoint.split(bstack11l11ll_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧḜ"))) > 1:
        ws_url = ws_endpoint.split(bstack11l11ll_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨḝ"))[0]
        if bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭Ḟ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack1111lll1lll_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack11l11ll_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪḟ"))[1]))
            bstack1111lll1lll_opy_ = bstack1111lll1lll_opy_ or {}
            bstack1lll1111l1_opy_ = os.environ[bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪḠ")]
            bstack1111lll1lll_opy_[bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧḡ")] = str(framework) + str(__version__)
            bstack1111lll1lll_opy_[bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨḢ")] = bstack1lll1l11l11_opy_()
            bstack1111lll1lll_opy_[bstack11l11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪḣ")] = bstack1lll1111l1_opy_
            bstack1111lll1lll_opy_[bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪḤ")] = bstack11111l11l_opy_
            ws_endpoint = ws_endpoint.split(bstack11l11ll_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩḥ"))[0] + bstack11l11ll_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪḦ") + urllib.parse.quote(json.dumps(bstack1111lll1lll_opy_))
    return ws_endpoint
def bstack1l11l1l11_opy_():
    global bstack1ll1ll1ll_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1ll1ll1ll_opy_ = BrowserType.connect
    return bstack1ll1ll1ll_opy_
def bstack11111l1ll_opy_(framework_name):
    global bstack1ll11l111l_opy_
    bstack1ll11l111l_opy_ = framework_name
    return framework_name
def bstack1l1l11l11l_opy_(self, *args, **kwargs):
    global bstack1ll1ll1ll_opy_
    try:
        global bstack1ll11l111l_opy_
        if bstack11l11ll_opy_ (u"ࠬࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵࠩḧ") in kwargs:
            kwargs[bstack11l11ll_opy_ (u"࠭ࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶࠪḨ")] = bstack1111lll1111_opy_(
                kwargs.get(bstack11l11ll_opy_ (u"ࠧࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷࠫḩ"), None),
                bstack1ll11l111l_opy_
            )
    except Exception as e:
        logger.error(bstack11l11ll_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪࡨࡲࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡖࡈࡐࠦࡣࡢࡲࡶ࠾ࠥࢁࡽࠣḪ").format(str(e)))
    return bstack1ll1ll1ll_opy_(self, *args, **kwargs)
def bstack111l11l1l1l_opy_(bstack1111lllll1l_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1l1ll111ll_opy_(bstack1111lllll1l_opy_, bstack11l11ll_opy_ (u"ࠤࠥḫ"))
        if proxies and proxies.get(bstack11l11ll_opy_ (u"ࠥ࡬ࡹࡺࡰࡴࠤḬ")):
            parsed_url = urlparse(proxies.get(bstack11l11ll_opy_ (u"ࠦ࡭ࡺࡴࡱࡵࠥḭ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack11l11ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࡌࡴࡹࡴࠨḮ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack11l11ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡵࡲࡵࠩḯ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack11l11ll_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡛ࡳࡦࡴࠪḰ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack11l11ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡢࡵࡶࠫḱ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1l1l1ll1l1_opy_(bstack1111lllll1l_opy_):
    bstack1111ll1l111_opy_ = {
        bstack11l1l11l1ll_opy_[bstack1111l11llll_opy_]: bstack1111lllll1l_opy_[bstack1111l11llll_opy_]
        for bstack1111l11llll_opy_ in bstack1111lllll1l_opy_
        if bstack1111l11llll_opy_ in bstack11l1l11l1ll_opy_
    }
    bstack1111ll1l111_opy_[bstack11l11ll_opy_ (u"ࠤࡳࡶࡴࡾࡹࡔࡧࡷࡸ࡮ࡴࡧࡴࠤḲ")] = bstack111l11l1l1l_opy_(bstack1111lllll1l_opy_, bstack1lll11111_opy_.get_property(bstack11l11ll_opy_ (u"ࠥࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵࠥḳ")))
    bstack111l11l1ll1_opy_ = [element.lower() for element in bstack11l11ll1ll1_opy_]
    bstack111l11ll1l1_opy_(bstack1111ll1l111_opy_, bstack111l11l1ll1_opy_)
    return bstack1111ll1l111_opy_
def bstack111l11ll1l1_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack11l11ll_opy_ (u"ࠦ࠯࠰ࠪࠫࠤḴ")
    for value in d.values():
        if isinstance(value, dict):
            bstack111l11ll1l1_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack111l11ll1l1_opy_(item, keys)
def bstack1ll111lll11_opy_():
    bstack1111ll1lll1_opy_ = [os.environ.get(bstack11l11ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡏࡌࡆࡕࡢࡈࡎࡘࠢḵ")), os.path.join(os.path.expanduser(bstack11l11ll_opy_ (u"ࠨࡾࠣḶ")), bstack11l11ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧḷ")), os.path.join(bstack11l11ll_opy_ (u"ࠨ࠱ࡷࡱࡵ࠭Ḹ"), bstack11l11ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩḹ"))]
    for path in bstack1111ll1lll1_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack11l11ll_opy_ (u"ࠥࡊ࡮ࡲࡥࠡࠩࠥḺ") + str(path) + bstack11l11ll_opy_ (u"ࠦࠬࠦࡥࡹ࡫ࡶࡸࡸ࠴ࠢḻ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack11l11ll_opy_ (u"ࠧࡍࡩࡷ࡫ࡱ࡫ࠥࡶࡥࡳ࡯࡬ࡷࡸ࡯࡯࡯ࡵࠣࡪࡴࡸࠠࠨࠤḼ") + str(path) + bstack11l11ll_opy_ (u"ࠨࠧࠣḽ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack11l11ll_opy_ (u"ࠢࡇ࡫࡯ࡩࠥ࠭ࠢḾ") + str(path) + bstack11l11ll_opy_ (u"ࠣࠩࠣࡥࡱࡸࡥࡢࡦࡼࠤ࡭ࡧࡳࠡࡶ࡫ࡩࠥࡸࡥࡲࡷ࡬ࡶࡪࡪࠠࡱࡧࡵࡱ࡮ࡹࡳࡪࡱࡱࡷ࠳ࠨḿ"))
            else:
                logger.debug(bstack11l11ll_opy_ (u"ࠤࡆࡶࡪࡧࡴࡪࡰࡪࠤ࡫࡯࡬ࡦࠢࠪࠦṀ") + str(path) + bstack11l11ll_opy_ (u"ࠥࠫࠥࡽࡩࡵࡪࠣࡻࡷ࡯ࡴࡦࠢࡳࡩࡷࡳࡩࡴࡵ࡬ࡳࡳ࠴ࠢṁ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack11l11ll_opy_ (u"ࠦࡔࡶࡥࡳࡣࡷ࡭ࡴࡴࠠࡴࡷࡦࡧࡪ࡫ࡤࡦࡦࠣࡪࡴࡸࠠࠨࠤṂ") + str(path) + bstack11l11ll_opy_ (u"ࠧ࠭࠮ࠣṃ"))
            return path
        except Exception as e:
            logger.debug(bstack11l11ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡵࡱࠢࡩ࡭ࡱ࡫ࠠࠨࡽࡳࡥࡹ࡮ࡽࠨ࠼ࠣࠦṄ") + str(e) + bstack11l11ll_opy_ (u"ࠢࠣṅ"))
    logger.debug(bstack11l11ll_opy_ (u"ࠣࡃ࡯ࡰࠥࡶࡡࡵࡪࡶࠤ࡫ࡧࡩ࡭ࡧࡧ࠲ࠧṆ"))
    return None
@measure(event_name=EVENTS.bstack11l11ll1lll_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
def bstack1l1l1ll1ll1_opy_(binary_path, bstack1l1l11111ll_opy_, bs_config):
    logger.debug(bstack11l11ll_opy_ (u"ࠤࡆࡹࡷࡸࡥ࡯ࡶࠣࡇࡑࡏࠠࡑࡣࡷ࡬ࠥ࡬࡯ࡶࡰࡧ࠾ࠥࢁࡽࠣṇ").format(binary_path))
    bstack111l11l1111_opy_ = bstack11l11ll_opy_ (u"ࠪࠫṈ")
    bstack1111lllllll_opy_ = {
        bstack11l11ll_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩṉ"): __version__,
        bstack11l11ll_opy_ (u"ࠧࡵࡳࠣṊ"): platform.system(),
        bstack11l11ll_opy_ (u"ࠨ࡯ࡴࡡࡤࡶࡨ࡮ࠢṋ"): platform.machine(),
        bstack11l11ll_opy_ (u"ࠢࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧṌ"): bstack11l11ll_opy_ (u"ࠨ࠲ࠪṍ"),
        bstack11l11ll_opy_ (u"ࠤࡶࡨࡰࡥ࡬ࡢࡰࡪࡹࡦ࡭ࡥࠣṎ"): bstack11l11ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪṏ")
    }
    bstack1111l11l11l_opy_(bstack1111lllllll_opy_)
    try:
        if binary_path:
            bstack1111lllllll_opy_[bstack11l11ll_opy_ (u"ࠫࡨࡲࡩࡠࡸࡨࡶࡸ࡯࡯࡯ࠩṐ")] = subprocess.check_output([binary_path, bstack11l11ll_opy_ (u"ࠧࡼࡥࡳࡵ࡬ࡳࡳࠨṑ")]).strip().decode(bstack11l11ll_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬṒ"))
        response = requests.request(
            bstack11l11ll_opy_ (u"ࠧࡈࡇࡗࠫṓ"),
            url=bstack1l11lll1l1_opy_(bstack11l11lll1l1_opy_),
            headers=None,
            auth=(bs_config[bstack11l11ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪṔ")], bs_config[bstack11l11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬṕ")]),
            json=None,
            params=bstack1111lllllll_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack11l11ll_opy_ (u"ࠪࡹࡷࡲࠧṖ") in data.keys() and bstack11l11ll_opy_ (u"ࠫࡺࡶࡤࡢࡶࡨࡨࡤࡩ࡬ࡪࡡࡹࡩࡷࡹࡩࡰࡰࠪṗ") in data.keys():
            logger.debug(bstack11l11ll_opy_ (u"ࠧࡔࡥࡦࡦࠣࡸࡴࠦࡵࡱࡦࡤࡸࡪࠦࡢࡪࡰࡤࡶࡾ࠲ࠠࡤࡷࡵࡶࡪࡴࡴࠡࡤ࡬ࡲࡦࡸࡹࠡࡸࡨࡶࡸ࡯࡯࡯࠼ࠣࡿࢂࠨṘ").format(bstack1111lllllll_opy_[bstack11l11ll_opy_ (u"࠭ࡣ࡭࡫ࡢࡺࡪࡸࡳࡪࡱࡱࠫṙ")]))
            if bstack11l11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡊࡐࡄࡖ࡞ࡥࡕࡓࡎࠪṚ") in os.environ:
                logger.debug(bstack11l11ll_opy_ (u"ࠣࡕ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡦ࡮ࡴࡡࡳࡻࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡧࡳࠡࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡖࡔࡏࠤ࡮ࡹࠠࡴࡧࡷࠦṛ"))
                data[bstack11l11ll_opy_ (u"ࠩࡸࡶࡱ࠭Ṝ")] = os.environ[bstack11l11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡘࡖࡑ࠭ṝ")]
            bstack111l1l1llll_opy_ = bstack1111l1l1111_opy_(data[bstack11l11ll_opy_ (u"ࠫࡺࡸ࡬ࠨṞ")], bstack1l1l11111ll_opy_)
            bstack111l11l1111_opy_ = os.path.join(bstack1l1l11111ll_opy_, bstack111l1l1llll_opy_)
            os.chmod(bstack111l11l1111_opy_, 0o777) # bstack111l1l11ll1_opy_ permission
            return bstack111l11l1111_opy_
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡨࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡰࡨࡻ࡙ࠥࡄࡌࠢࡾࢁࠧṟ").format(e))
    return binary_path
def bstack1111l11l11l_opy_(bstack1111lllllll_opy_):
    try:
        if bstack11l11ll_opy_ (u"࠭࡬ࡪࡰࡸࡼࠬṠ") not in bstack1111lllllll_opy_[bstack11l11ll_opy_ (u"ࠧࡰࡵࠪṡ")].lower():
            return
        if os.path.exists(bstack11l11ll_opy_ (u"ࠣ࠱ࡨࡸࡨ࠵࡯ࡴ࠯ࡵࡩࡱ࡫ࡡࡴࡧࠥṢ")):
            with open(bstack11l11ll_opy_ (u"ࠤ࠲ࡩࡹࡩ࠯ࡰࡵ࠰ࡶࡪࡲࡥࡢࡵࡨࠦṣ"), bstack11l11ll_opy_ (u"ࠥࡶࠧṤ")) as f:
                bstack111l1l1ll11_opy_ = {}
                for line in f:
                    if bstack11l11ll_opy_ (u"ࠦࡂࠨṥ") in line:
                        key, value = line.rstrip().split(bstack11l11ll_opy_ (u"ࠧࡃࠢṦ"), 1)
                        bstack111l1l1ll11_opy_[key] = value.strip(bstack11l11ll_opy_ (u"࠭ࠢ࡝ࠩࠪṧ"))
                bstack1111lllllll_opy_[bstack11l11ll_opy_ (u"ࠧࡥ࡫ࡶࡸࡷࡵࠧṨ")] = bstack111l1l1ll11_opy_.get(bstack11l11ll_opy_ (u"ࠣࡋࡇࠦṩ"), bstack11l11ll_opy_ (u"ࠤࠥṪ"))
        elif os.path.exists(bstack11l11ll_opy_ (u"ࠥ࠳ࡪࡺࡣ࠰ࡣ࡯ࡴ࡮ࡴࡥ࠮ࡴࡨࡰࡪࡧࡳࡦࠤṫ")):
            bstack1111lllllll_opy_[bstack11l11ll_opy_ (u"ࠫࡩ࡯ࡳࡵࡴࡲࠫṬ")] = bstack11l11ll_opy_ (u"ࠬࡧ࡬ࡱ࡫ࡱࡩࠬṭ")
    except Exception as e:
        logger.debug(bstack11l11ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡹࠦࡤࡪࡵࡷࡶࡴࠦ࡯ࡧࠢ࡯࡭ࡳࡻࡸࠣṮ") + e)
@measure(event_name=EVENTS.bstack11l11llll1l_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
def bstack1111l1l1111_opy_(bstack111l11llll1_opy_, bstack1111lll1l11_opy_):
    logger.debug(bstack11l11ll_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡶࡴࡳ࠺ࠡࠤṯ") + str(bstack111l11llll1_opy_) + bstack11l11ll_opy_ (u"ࠣࠤṰ"))
    zip_path = os.path.join(bstack1111lll1l11_opy_, bstack11l11ll_opy_ (u"ࠤࡧࡳࡼࡴ࡬ࡰࡣࡧࡩࡩࡥࡦࡪ࡮ࡨ࠲ࡿ࡯ࡰࠣṱ"))
    bstack111l1l1llll_opy_ = bstack11l11ll_opy_ (u"ࠪࠫṲ")
    with requests.get(bstack111l11llll1_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack11l11ll_opy_ (u"ࠦࡼࡨࠢṳ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack11l11ll_opy_ (u"ࠧࡌࡩ࡭ࡧࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾ࠴ࠢṴ"))
    with zipfile.ZipFile(zip_path, bstack11l11ll_opy_ (u"࠭ࡲࠨṵ")) as zip_ref:
        bstack1111ll11lll_opy_ = zip_ref.namelist()
        if len(bstack1111ll11lll_opy_) > 0:
            bstack111l1l1llll_opy_ = bstack1111ll11lll_opy_[0] # bstack111l11lllll_opy_ bstack11l1l11111l_opy_ will be bstack111l1111lll_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack1111lll1l11_opy_)
        logger.debug(bstack11l11ll_opy_ (u"ࠢࡇ࡫࡯ࡩࡸࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽࠥ࡫ࡸࡵࡴࡤࡧࡹ࡫ࡤࠡࡶࡲࠤࠬࠨṶ") + str(bstack1111lll1l11_opy_) + bstack11l11ll_opy_ (u"ࠣࠩࠥṷ"))
    os.remove(zip_path)
    return bstack111l1l1llll_opy_
def get_cli_dir():
    bstack1111ll11l11_opy_ = bstack1ll111lll11_opy_()
    if bstack1111ll11l11_opy_:
        bstack1l1l11111ll_opy_ = os.path.join(bstack1111ll11l11_opy_, bstack11l11ll_opy_ (u"ࠤࡦࡰ࡮ࠨṸ"))
        if not os.path.exists(bstack1l1l11111ll_opy_):
            os.makedirs(bstack1l1l11111ll_opy_, mode=0o777, exist_ok=True)
        return bstack1l1l11111ll_opy_
    else:
        raise FileNotFoundError(bstack11l11ll_opy_ (u"ࠥࡒࡴࠦࡷࡳ࡫ࡷࡥࡧࡲࡥࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽ࠳ࠨṹ"))
def bstack1l1l11ll11l_opy_(bstack1l1l11111ll_opy_):
    bstack11l11ll_opy_ (u"ࠦࠧࠨࡇࡦࡶࠣࡸ࡭࡫ࠠࡱࡣࡷ࡬ࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯࡙ࠥࡄࡌࠢࡥ࡭ࡳࡧࡲࡺࠢ࡬ࡲࠥࡧࠠࡸࡴ࡬ࡸࡦࡨ࡬ࡦࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽ࠳ࠨࠢࠣṺ")
    bstack1111l11l111_opy_ = [
        os.path.join(bstack1l1l11111ll_opy_, f)
        for f in os.listdir(bstack1l1l11111ll_opy_)
        if os.path.isfile(os.path.join(bstack1l1l11111ll_opy_, f)) and f.startswith(bstack11l11ll_opy_ (u"ࠧࡨࡩ࡯ࡣࡵࡽ࠲ࠨṻ"))
    ]
    if len(bstack1111l11l111_opy_) > 0:
        return max(bstack1111l11l111_opy_, key=os.path.getmtime) # get bstack111l1l11l11_opy_ binary
    return bstack11l11ll_opy_ (u"ࠨࠢṼ")
def bstack1111l1ll1l1_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l111l11lll_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l111l11lll_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack11111l111l_opy_(data, keys, default=None):
    bstack11l11ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡔࡣࡩࡩࡱࡿࠠࡨࡧࡷࠤࡦࠦ࡮ࡦࡵࡷࡩࡩࠦࡶࡢ࡮ࡸࡩࠥ࡬ࡲࡰ࡯ࠣࡥࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺࠢࡲࡶࠥࡲࡩࡴࡶ࠱ࠎࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡࡦࡤࡸࡦࡀࠠࡕࡪࡨࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹࠡࡱࡵࠤࡱ࡯ࡳࡵࠢࡷࡳࠥࡺࡲࡢࡸࡨࡶࡸ࡫࠮ࠋࠢࠣࠤࠥࡀࡰࡢࡴࡤࡱࠥࡱࡥࡺࡵ࠽ࠤࡆࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠ࡬ࡧࡼࡷ࠴࡯࡮ࡥ࡫ࡦࡩࡸࠦࡲࡦࡲࡵࡩࡸ࡫࡮ࡵ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡳࡥࡹ࡮࠮ࠋࠢࠣࠤࠥࡀࡰࡢࡴࡤࡱࠥࡪࡥࡧࡣࡸࡰࡹࡀࠠࡗࡣ࡯ࡹࡪࠦࡴࡰࠢࡵࡩࡹࡻࡲ࡯ࠢ࡬ࡪࠥࡺࡨࡦࠢࡳࡥࡹ࡮ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴ࠯ࠌࠣࠤࠥࠦ࠺ࡳࡧࡷࡹࡷࡴ࠺ࠡࡖ࡫ࡩࠥࡼࡡ࡭ࡷࡨࠤࡦࡺࠠࡵࡪࡨࠤࡳ࡫ࡳࡵࡧࡧࠤࡵࡧࡴࡩ࠮ࠣࡳࡷࠦࡤࡦࡨࡤࡹࡱࡺࠠࡪࡨࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠴ࠊࠡࠢࠣࠤࠧࠨࠢṽ")
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