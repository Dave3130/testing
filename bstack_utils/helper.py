# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
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
from bstack_utils.constants import (bstack1lll1l1ll1_opy_, bstack1ll111111l_opy_, bstack111lll11l1_opy_,
                                    bstack11l11llllll_opy_, bstack11l1l1l11l1_opy_, bstack11l11llll11_opy_, bstack11l11lll111_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1lll11l1ll_opy_, bstack11lll11l1_opy_
from bstack_utils.proxy import bstack1ll111lll_opy_, bstack111l11ll1_opy_
from bstack_utils.constants import *
from bstack_utils import bstack11llll111l_opy_
from bstack_utils.bstack1l11l1l111_opy_ import bstack1l111ll1l1_opy_
from browserstack_sdk._version import __version__
bstack1lll1ll1l_opy_ = Config.bstack1111l1ll_opy_()
logger = bstack11llll111l_opy_.get_logger(__name__, bstack11llll111l_opy_.bstack1l1l11l11ll_opy_())
def bstack1111ll11111_opy_(config):
    return config[bstack1lllll1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩᯫ")]
def bstack111l111ll11_opy_(config):
    return config[bstack1lllll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫᯬ")]
def bstack1llllll111_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack1111ll1111l_opy_(obj):
    values = []
    bstack1111ll1lll1_opy_ = re.compile(bstack1lllll1l_opy_ (u"ࡴࠥࡢࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࡞ࡧ࠯ࠩࠨᯭ"), re.I)
    for key in obj.keys():
        if bstack1111ll1lll1_opy_.match(key):
            values.append(obj[key])
    return values
def bstack111l1lll11l_opy_(config):
    tags = []
    tags.extend(bstack1111ll1111l_opy_(os.environ))
    tags.extend(bstack1111ll1111l_opy_(config))
    return tags
def bstack111l1l1l1l1_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111l1l1111l_opy_(bstack111l111l11l_opy_):
    if not bstack111l111l11l_opy_:
        return bstack1lllll1l_opy_ (u"ࠪࠫᯮ")
    return bstack1lllll1l_opy_ (u"ࠦࢀࢃࠠࠩࡽࢀ࠭ࠧᯯ").format(bstack111l111l11l_opy_.name, bstack111l111l11l_opy_.email)
def bstack1111lll1l1l_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack1111ll1l11l_opy_ = repo.common_dir
        info = {
            bstack1lllll1l_opy_ (u"ࠧࡹࡨࡢࠤᯰ"): repo.head.commit.hexsha,
            bstack1lllll1l_opy_ (u"ࠨࡳࡩࡱࡵࡸࡤࡹࡨࡢࠤᯱ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack1lllll1l_opy_ (u"ࠢࡣࡴࡤࡲࡨ࡮᯲ࠢ"): repo.active_branch.name,
            bstack1lllll1l_opy_ (u"ࠣࡶࡤ࡫᯳ࠧ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack1lllll1l_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡶࡨࡶࠧ᯴"): bstack111l1l1111l_opy_(repo.head.commit.committer),
            bstack1lllll1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡷࡩࡷࡥࡤࡢࡶࡨࠦ᯵"): repo.head.commit.committed_datetime.isoformat(),
            bstack1lllll1l_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࠦ᯶"): bstack111l1l1111l_opy_(repo.head.commit.author),
            bstack1lllll1l_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡤࡪࡡࡵࡧࠥ᯷"): repo.head.commit.authored_datetime.isoformat(),
            bstack1lllll1l_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢ᯸"): repo.head.commit.message,
            bstack1lllll1l_opy_ (u"ࠢࡳࡱࡲࡸࠧ᯹"): repo.git.rev_parse(bstack1lllll1l_opy_ (u"ࠣ࠯࠰ࡷ࡭ࡵࡷ࠮ࡶࡲࡴࡱ࡫ࡶࡦ࡮ࠥ᯺")),
            bstack1lllll1l_opy_ (u"ࠤࡦࡳࡲࡳ࡯࡯ࡡࡪ࡭ࡹࡥࡤࡪࡴࠥ᯻"): bstack1111ll1l11l_opy_,
            bstack1lllll1l_opy_ (u"ࠥࡻࡴࡸ࡫ࡵࡴࡨࡩࡤ࡭ࡩࡵࡡࡧ࡭ࡷࠨ᯼"): subprocess.check_output([bstack1lllll1l_opy_ (u"ࠦ࡬࡯ࡴࠣ᯽"), bstack1lllll1l_opy_ (u"ࠧࡸࡥࡷ࠯ࡳࡥࡷࡹࡥࠣ᯾"), bstack1lllll1l_opy_ (u"ࠨ࠭࠮ࡩ࡬ࡸ࠲ࡩ࡯࡮࡯ࡲࡲ࠲ࡪࡩࡳࠤ᯿")]).strip().decode(
                bstack1lllll1l_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᰀ")),
            bstack1lllll1l_opy_ (u"ࠣ࡮ࡤࡷࡹࡥࡴࡢࡩࠥᰁ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack1lllll1l_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡵࡢࡷ࡮ࡴࡣࡦࡡ࡯ࡥࡸࡺ࡟ࡵࡣࡪࠦᰂ"): repo.git.rev_list(
                bstack1lllll1l_opy_ (u"ࠥࡿࢂ࠴࠮ࡼࡿࠥᰃ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1111lllll1l_opy_ = []
        for remote in remotes:
            bstack1111lll11ll_opy_ = {
                bstack1lllll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᰄ"): remote.name,
                bstack1lllll1l_opy_ (u"ࠧࡻࡲ࡭ࠤᰅ"): remote.url,
            }
            bstack1111lllll1l_opy_.append(bstack1111lll11ll_opy_)
        bstack111l11l11ll_opy_ = {
            bstack1lllll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᰆ"): bstack1lllll1l_opy_ (u"ࠢࡨ࡫ࡷࠦᰇ"),
            **info,
            bstack1lllll1l_opy_ (u"ࠣࡴࡨࡱࡴࡺࡥࡴࠤᰈ"): bstack1111lllll1l_opy_
        }
        bstack111l11l11ll_opy_ = bstack111l11111ll_opy_(bstack111l11l11ll_opy_)
        return bstack111l11l11ll_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack1lllll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡲࡴࡺࡲࡡࡵ࡫ࡱ࡫ࠥࡍࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧᰉ").format(err))
        return {}
def bstack11ll1l1l1ll_opy_(bstack111l1ll111l_opy_=None):
    bstack1lllll1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡋࡪࡺࠠࡨ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡳࡱࡧࡦ࡭࡫࡯ࡣࡢ࡮࡯ࡽࠥ࡬࡯ࡳ࡯ࡤࡸࡹ࡫ࡤࠡࡨࡲࡶࠥࡇࡉࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱࠤࡺࡹࡥࠡࡥࡤࡷࡪࡹࠠࡧࡱࡵࠤࡪࡧࡣࡩࠢࡩࡳࡱࡪࡥࡳࠢ࡬ࡲࠥࡺࡨࡦࠢ࡯࡭ࡸࡺ࠮ࠋࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࡬࡯࡭ࡦࡨࡶࡸࠦࠨ࡭࡫ࡶࡸ࠱ࠦ࡯ࡱࡶ࡬ࡳࡳࡧ࡬ࠪ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤ࡫ࡵ࡬ࡥࡧࡵࠤࡵࡧࡴࡩࡵࠣࡸࡴࠦࡥࡹࡶࡵࡥࡨࡺࠠࡨ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡦࡳࡱࡰ࠲ࠥࡊࡥࡧࡣࡸࡰࡹࡹࠠࡵࡱࠣ࡟ࡴࡹ࠮ࡨࡧࡷࡧࡼࡪࠨࠪ࡟࠱ࠎࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡱ࡯ࡳࡵ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡩ࡯ࡣࡵࡵ࠯ࠤࡪࡧࡣࡩࠢࡦࡳࡳࡺࡡࡪࡰ࡬ࡲ࡬ࠦࡧࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡤࠤ࡫ࡵ࡬ࡥࡧࡵ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᰊ")
    if bstack111l1ll111l_opy_ == None: # bstack1111ll11ll1_opy_ for bstack11ll1ll11l1_opy_-repo
        bstack111l1ll111l_opy_ = [os.getcwd()]
    results = []
    for folder in bstack111l1ll111l_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack1lllll1l_opy_ (u"ࠦࡵࡸࡉࡥࠤᰋ"): bstack1lllll1l_opy_ (u"ࠧࠨᰌ"),
                bstack1lllll1l_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧᰍ"): [],
                bstack1lllll1l_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࡳࠣᰎ"): [],
                bstack1lllll1l_opy_ (u"ࠣࡲࡵࡈࡦࡺࡥࠣᰏ"): bstack1lllll1l_opy_ (u"ࠤࠥᰐ"),
                bstack1lllll1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡐࡩࡸࡹࡡࡨࡧࡶࠦᰑ"): [],
                bstack1lllll1l_opy_ (u"ࠦࡵࡸࡔࡪࡶ࡯ࡩࠧᰒ"): bstack1lllll1l_opy_ (u"ࠧࠨᰓ"),
                bstack1lllll1l_opy_ (u"ࠨࡰࡳࡆࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࠨᰔ"): bstack1lllll1l_opy_ (u"ࠢࠣᰕ"),
                bstack1lllll1l_opy_ (u"ࠣࡲࡵࡖࡦࡽࡄࡪࡨࡩࠦᰖ"): bstack1lllll1l_opy_ (u"ࠤࠥᰗ")
            }
            bstack111l111l1ll_opy_ = repo.active_branch.name
            bstack111l1l11111_opy_ = repo.head.commit
            result[bstack1lllll1l_opy_ (u"ࠥࡴࡷࡏࡤࠣᰘ")] = bstack111l1l11111_opy_.hexsha
            bstack111l1111l11_opy_ = _111l111lll1_opy_(repo)
            logger.debug(bstack1lllll1l_opy_ (u"ࠦࡇࡧࡳࡦࠢࡥࡶࡦࡴࡣࡩࠢࡩࡳࡷࠦࡣࡰ࡯ࡳࡥࡷ࡯ࡳࡰࡰ࠽ࠤࠧᰙ") + str(bstack111l1111l11_opy_) + bstack1lllll1l_opy_ (u"ࠧࠨᰚ"))
            if bstack111l1111l11_opy_:
                try:
                    bstack1111l11l1ll_opy_ = repo.git.diff(bstack1lllll1l_opy_ (u"ࠨ࠭࠮ࡰࡤࡱࡪ࠳࡯࡯࡮ࡼࠦᰛ"), bstack11ll1l1l_opy_ (u"ࠢࡼࡤࡤࡷࡪࡥࡢࡳࡣࡱࡧ࡭ࢃ࠮࠯࠰ࡾࡧࡺࡸࡲࡦࡰࡷࡣࡧࡸࡡ࡯ࡥ࡫ࢁࠧᰜ")).split(bstack1lllll1l_opy_ (u"ࠨ࡞ࡱࠫᰝ"))
                    logger.debug(bstack1lllll1l_opy_ (u"ࠤࡆ࡬ࡦࡴࡧࡦࡦࠣࡪ࡮ࡲࡥࡴࠢࡥࡩࡹࡽࡥࡦࡰࠣࡿࡧࡧࡳࡦࡡࡥࡶࡦࡴࡣࡩࡿࠣࡥࡳࡪࠠࡼࡥࡸࡶࡷ࡫࡮ࡵࡡࡥࡶࡦࡴࡣࡩࡿ࠽ࠤࠧᰞ") + str(bstack1111l11l1ll_opy_) + bstack1lllll1l_opy_ (u"ࠥࠦᰟ"))
                    result[bstack1lllll1l_opy_ (u"ࠦ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠥᰠ")] = [f.strip() for f in bstack1111l11l1ll_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack11ll1l1l_opy_ (u"ࠧࢁࡢࡢࡵࡨࡣࡧࡸࡡ࡯ࡥ࡫ࢁ࠳࠴ࡻࡤࡷࡵࡶࡪࡴࡴࡠࡤࡵࡥࡳࡩࡨࡾࠤᰡ")))
                except Exception:
                    logger.debug(bstack1lllll1l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡪࡩࡹࠦࡣࡩࡣࡱ࡫ࡪࡪࠠࡧ࡫࡯ࡩࡸࠦࡦࡳࡱࡰࠤࡧࡸࡡ࡯ࡥ࡫ࠤࡨࡵ࡭ࡱࡣࡵ࡭ࡸࡵ࡮࠯ࠢࡉࡥࡱࡲࡩ࡯ࡩࠣࡦࡦࡩ࡫ࠡࡶࡲࠤࡷ࡫ࡣࡦࡰࡷࠤࡨࡵ࡭࡮࡫ࡷࡷ࠳ࠨᰢ"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack1lllll1l_opy_ (u"ࠢࡧ࡫࡯ࡩࡸࡉࡨࡢࡰࡪࡩࡩࠨᰣ")] = _1111l1l11ll_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack1lllll1l_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢᰤ")] = _1111l1l11ll_opy_(commits[:5])
            bstack111l111l111_opy_ = set()
            bstack1111ll11l1l_opy_ = []
            for commit in commits:
                logger.debug(bstack1lllll1l_opy_ (u"ࠤࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡣࡰ࡯ࡰ࡭ࡹࡀࠠࠣᰥ") + str(commit.message) + bstack1lllll1l_opy_ (u"ࠥࠦᰦ"))
                bstack111l1l111l1_opy_ = commit.author.name if commit.author else bstack1lllll1l_opy_ (u"࡚ࠦࡴ࡫࡯ࡱࡺࡲࠧᰧ")
                bstack111l111l111_opy_.add(bstack111l1l111l1_opy_)
                bstack1111ll11l1l_opy_.append({
                    bstack1lllll1l_opy_ (u"ࠧࡳࡥࡴࡵࡤ࡫ࡪࠨᰨ"): commit.message.strip(),
                    bstack1lllll1l_opy_ (u"ࠨࡵࡴࡧࡵࠦᰩ"): bstack111l1l111l1_opy_
                })
            result[bstack1lllll1l_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸࡳࠣᰪ")] = list(bstack111l111l111_opy_)
            result[bstack1lllll1l_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡎࡧࡶࡷࡦ࡭ࡥࡴࠤᰫ")] = bstack1111ll11l1l_opy_
            result[bstack1lllll1l_opy_ (u"ࠤࡳࡶࡉࡧࡴࡦࠤᰬ")] = bstack111l1l11111_opy_.committed_datetime.strftime(bstack1lllll1l_opy_ (u"ࠥࠩ࡞࠳ࠥ࡮࠯ࠨࡨࠧᰭ"))
            if (not result[bstack1lllll1l_opy_ (u"ࠦࡵࡸࡔࡪࡶ࡯ࡩࠧᰮ")] or result[bstack1lllll1l_opy_ (u"ࠧࡶࡲࡕ࡫ࡷࡰࡪࠨᰯ")].strip() == bstack1lllll1l_opy_ (u"ࠨࠢᰰ")) and bstack111l1l11111_opy_.message:
                bstack111l11111l1_opy_ = bstack111l1l11111_opy_.message.strip().splitlines()
                result[bstack1lllll1l_opy_ (u"ࠢࡱࡴࡗ࡭ࡹࡲࡥࠣᰱ")] = bstack111l11111l1_opy_[0] if bstack111l11111l1_opy_ else bstack1lllll1l_opy_ (u"ࠣࠤᰲ")
                if len(bstack111l11111l1_opy_) > 2:
                    result[bstack1lllll1l_opy_ (u"ࠤࡳࡶࡉ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠤᰳ")] = bstack1lllll1l_opy_ (u"ࠪࡠࡳ࠭ᰴ").join(bstack111l11111l1_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack1lllll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡴࡶࡵ࡭ࡣࡷ࡭ࡳ࡭ࠠࡈ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡦࡰࡴࠣࡅࡎࠦࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠢࠫࡪࡴࡲࡤࡦࡴ࠽ࠤࢀ࡬࡯࡭ࡦࡨࡶࢂ࠯࠺ࠡࠤᰵ") + str(err) + bstack1lllll1l_opy_ (u"ࠧࠨᰶ"))
    filtered_results = [
        result
        for result in results
        if _1111ll11lll_opy_(result)
    ]
    return filtered_results
def _1111ll11lll_opy_(result):
    bstack1lllll1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡈࡦ࡮ࡳࡩࡷࠦࡴࡰࠢࡦ࡬ࡪࡩ࡫ࠡ࡫ࡩࠤࡦࠦࡧࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥࡸࡥࡴࡷ࡯ࡸࠥ࡯ࡳࠡࡸࡤࡰ࡮ࡪࠠࠩࡰࡲࡲ࠲࡫࡭ࡱࡶࡼࠤ࡫࡯࡬ࡦࡵࡆ࡬ࡦࡴࡧࡦࡦࠣࡥࡳࡪࠠࡢࡷࡷ࡬ࡴࡸࡳࠪ࠰ࠍࠤࠥࠦࠠࠣࠤ᰷ࠥ")
    return (
        isinstance(result.get(bstack1lllll1l_opy_ (u"ࠢࡧ࡫࡯ࡩࡸࡉࡨࡢࡰࡪࡩࡩࠨ᰸"), None), list)
        and len(result[bstack1lllll1l_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢ᰹")]) > 0
        and isinstance(result.get(bstack1lllll1l_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡵࠥ᰺"), None), list)
        and len(result[bstack1lllll1l_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡶࠦ᰻")]) > 0
    )
def _111l111lll1_opy_(repo):
    bstack1lllll1l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤ࡙ࡸࡹࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡵࡪࡨࠤࡧࡧࡳࡦࠢࡥࡶࡦࡴࡣࡩࠢࡩࡳࡷࠦࡴࡩࡧࠣ࡫࡮ࡼࡥ࡯ࠢࡵࡩࡵࡵࠠࡸ࡫ࡷ࡬ࡴࡻࡴࠡࡪࡤࡶࡩࡩ࡯ࡥࡧࡧࠤࡳࡧ࡭ࡦࡵࠣࡥࡳࡪࠠࡸࡱࡵ࡯ࠥࡽࡩࡵࡪࠣࡥࡱࡲࠠࡗࡅࡖࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡷࡹ࠮ࠋࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࠦࡴࡩࡧࠣࡨࡪ࡬ࡡࡶ࡮ࡷࠤࡧࡸࡡ࡯ࡥ࡫ࠤ࡮࡬ࠠࡱࡱࡶࡷ࡮ࡨ࡬ࡦ࠮ࠣࡩࡱࡹࡥࠡࡐࡲࡲࡪ࠴ࠊࠡࠢࠣࠤࠧࠨࠢ᰼")
    try:
        try:
            origin = repo.remotes.origin
            bstack111l1ll1lll_opy_ = origin.refs[bstack1lllll1l_opy_ (u"ࠬࡎࡅࡂࡆࠪ᰽")]
            target = bstack111l1ll1lll_opy_.reference.name
            if target.startswith(bstack1lllll1l_opy_ (u"࠭࡯ࡳ࡫ࡪ࡭ࡳ࠵ࠧ᰾")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack1lllll1l_opy_ (u"ࠧࡰࡴ࡬࡫࡮ࡴ࠯ࠨ᰿")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _1111l1l11ll_opy_(commits):
    bstack1lllll1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡉࡨࡸࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡣࡩࡣࡱ࡫ࡪࡪࠠࡧ࡫࡯ࡩࡸࠦࡦࡳࡱࡰࠤࡦࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡤࡱࡰࡱ࡮ࡺࡳ࠯ࠌࠣࠤࠥࠦࠢࠣࠤ᱀")
    bstack1111l11l1ll_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack111l1111l1l_opy_ in diff:
                        if bstack111l1111l1l_opy_.a_path:
                            bstack1111l11l1ll_opy_.add(bstack111l1111l1l_opy_.a_path)
                        if bstack111l1111l1l_opy_.b_path:
                            bstack1111l11l1ll_opy_.add(bstack111l1111l1l_opy_.b_path)
    except Exception:
        pass
    return list(bstack1111l11l1ll_opy_)
def bstack111l11111ll_opy_(bstack111l11l11ll_opy_):
    bstack111l1l1llll_opy_ = bstack1111ll1l1ll_opy_(bstack111l11l11ll_opy_)
    if bstack111l1l1llll_opy_ and bstack111l1l1llll_opy_ > bstack11l11llllll_opy_:
        bstack111l1l11ll1_opy_ = bstack111l1l1llll_opy_ - bstack11l11llllll_opy_
        bstack1111l1l1111_opy_ = bstack111l1l1lll1_opy_(bstack111l11l11ll_opy_[bstack1lllll1l_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡡࡰࡩࡸࡹࡡࡨࡧࠥ᱁")], bstack111l1l11ll1_opy_)
        bstack111l11l11ll_opy_[bstack1lllll1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡢࡱࡪࡹࡳࡢࡩࡨࠦ᱂")] = bstack1111l1l1111_opy_
        logger.info(bstack1lllll1l_opy_ (u"࡙ࠦ࡮ࡥࠡࡥࡲࡱࡲ࡯ࡴࠡࡪࡤࡷࠥࡨࡥࡦࡰࠣࡸࡷࡻ࡮ࡤࡣࡷࡩࡩ࠴ࠠࡔ࡫ࡽࡩࠥࡵࡦࠡࡥࡲࡱࡲ࡯ࡴࠡࡣࡩࡸࡪࡸࠠࡵࡴࡸࡲࡨࡧࡴࡪࡱࡱࠤ࡮ࡹࠠࡼࡿࠣࡏࡇࠨ᱃")
                    .format(bstack1111ll1l1ll_opy_(bstack111l11l11ll_opy_) / 1024))
    return bstack111l11l11ll_opy_
def bstack1111ll1l1ll_opy_(json_data):
    try:
        if json_data:
            bstack111l1l11lll_opy_ = json.dumps(json_data)
            bstack1111ll111l1_opy_ = sys.getsizeof(bstack111l1l11lll_opy_)
            return bstack1111ll111l1_opy_
    except Exception as e:
        logger.debug(bstack1lllll1l_opy_ (u"࡙ࠧ࡯࡮ࡧࡷ࡬࡮ࡴࡧࠡࡹࡨࡲࡹࠦࡷࡳࡱࡱ࡫ࠥࡽࡨࡪ࡮ࡨࠤࡨࡧ࡬ࡤࡷ࡯ࡥࡹ࡯࡮ࡨࠢࡶ࡭ࡿ࡫ࠠࡰࡨࠣࡎࡘࡕࡎࠡࡱࡥ࡮ࡪࡩࡴ࠻ࠢࡾࢁࠧ᱄").format(e))
    return -1
def bstack111l1l1lll1_opy_(field, bstack111l1l11l1l_opy_):
    try:
        bstack1111l1l11l1_opy_ = len(bytes(bstack11l1l1l11l1_opy_, bstack1lllll1l_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬ᱅")))
        bstack1111l1ll111_opy_ = bytes(field, bstack1lllll1l_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭᱆"))
        bstack111l11l11l1_opy_ = len(bstack1111l1ll111_opy_)
        bstack1111l1l1l1l_opy_ = ceil(bstack111l11l11l1_opy_ - bstack111l1l11l1l_opy_ - bstack1111l1l11l1_opy_)
        if bstack1111l1l1l1l_opy_ > 0:
            bstack1111l11ll11_opy_ = bstack1111l1ll111_opy_[:bstack1111l1l1l1l_opy_].decode(bstack1lllll1l_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧ᱇"), errors=bstack1lllll1l_opy_ (u"ࠩ࡬࡫ࡳࡵࡲࡦࠩ᱈")) + bstack11l1l1l11l1_opy_
            return bstack1111l11ll11_opy_
    except Exception as e:
        logger.debug(bstack1lllll1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡶࡵࡹࡳࡩࡡࡵ࡫ࡱ࡫ࠥ࡬ࡩࡦ࡮ࡧ࠰ࠥࡴ࡯ࡵࡪ࡬ࡲ࡬ࠦࡷࡢࡵࠣࡸࡷࡻ࡮ࡤࡣࡷࡩࡩࠦࡨࡦࡴࡨ࠾ࠥࢁࡽࠣ᱉").format(e))
    return field
def bstack1l1l11llll_opy_():
    env = os.environ
    if (bstack1lllll1l_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤ࡛ࡒࡍࠤ᱊") in env and len(env[bstack1lllll1l_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡕࡓࡎࠥ᱋")]) > 0) or (
            bstack1lllll1l_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡉࡑࡐࡉࠧ᱌") in env and len(env[bstack1lllll1l_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡊࡒࡑࡊࠨᱍ")]) > 0):
        return {
            bstack1lllll1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᱎ"): bstack1lllll1l_opy_ (u"ࠤࡍࡩࡳࡱࡩ࡯ࡵࠥᱏ"),
            bstack1lllll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᱐"): env.get(bstack1lllll1l_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢ᱑")),
            bstack1lllll1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᱒"): env.get(bstack1lllll1l_opy_ (u"ࠨࡊࡐࡄࡢࡒࡆࡓࡅࠣ᱓")),
            bstack1lllll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᱔"): env.get(bstack1lllll1l_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢ᱕"))
        }
    if env.get(bstack1lllll1l_opy_ (u"ࠤࡆࡍࠧ᱖")) == bstack1lllll1l_opy_ (u"ࠥࡸࡷࡻࡥࠣ᱗") and bstack1111l11l1l_opy_(env.get(bstack1lllll1l_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡇࡎࠨ᱘"))):
        return {
            bstack1lllll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᱙"): bstack1lllll1l_opy_ (u"ࠨࡃࡪࡴࡦࡰࡪࡉࡉࠣᱚ"),
            bstack1lllll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᱛ"): env.get(bstack1lllll1l_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᱜ")),
            bstack1lllll1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᱝ"): env.get(bstack1lllll1l_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡎࡔࡈࠢᱞ")),
            bstack1lllll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᱟ"): env.get(bstack1lllll1l_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࠣᱠ"))
        }
    if env.get(bstack1lllll1l_opy_ (u"ࠨࡃࡊࠤᱡ")) == bstack1lllll1l_opy_ (u"ࠢࡵࡴࡸࡩࠧᱢ") and bstack1111l11l1l_opy_(env.get(bstack1lllll1l_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࠣᱣ"))):
        return {
            bstack1lllll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᱤ"): bstack1lllll1l_opy_ (u"ࠥࡘࡷࡧࡶࡪࡵࠣࡇࡎࠨᱥ"),
            bstack1lllll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᱦ"): env.get(bstack1lllll1l_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࡤࡈࡕࡊࡎࡇࡣ࡜ࡋࡂࡠࡗࡕࡐࠧᱧ")),
            bstack1lllll1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᱨ"): env.get(bstack1lllll1l_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᱩ")),
            bstack1lllll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᱪ"): env.get(bstack1lllll1l_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᱫ"))
        }
    if env.get(bstack1lllll1l_opy_ (u"ࠥࡇࡎࠨᱬ")) == bstack1lllll1l_opy_ (u"ࠦࡹࡸࡵࡦࠤᱭ") and env.get(bstack1lllll1l_opy_ (u"ࠧࡉࡉࡠࡐࡄࡑࡊࠨᱮ")) == bstack1lllll1l_opy_ (u"ࠨࡣࡰࡦࡨࡷ࡭࡯ࡰࠣᱯ"):
        return {
            bstack1lllll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᱰ"): bstack1lllll1l_opy_ (u"ࠣࡅࡲࡨࡪࡹࡨࡪࡲࠥᱱ"),
            bstack1lllll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᱲ"): None,
            bstack1lllll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᱳ"): None,
            bstack1lllll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᱴ"): None
        }
    if env.get(bstack1lllll1l_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡄࡕࡅࡓࡉࡈࠣᱵ")) and env.get(bstack1lllll1l_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡆࡓࡒࡓࡉࡕࠤᱶ")):
        return {
            bstack1lllll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᱷ"): bstack1lllll1l_opy_ (u"ࠣࡄ࡬ࡸࡧࡻࡣ࡬ࡧࡷࠦᱸ"),
            bstack1lllll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᱹ"): env.get(bstack1lllll1l_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡇࡊࡖࡢࡌ࡙࡚ࡐࡠࡑࡕࡍࡌࡏࡎࠣᱺ")),
            bstack1lllll1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᱻ"): None,
            bstack1lllll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᱼ"): env.get(bstack1lllll1l_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᱽ"))
        }
    if env.get(bstack1lllll1l_opy_ (u"ࠢࡄࡋࠥ᱾")) == bstack1lllll1l_opy_ (u"ࠣࡶࡵࡹࡪࠨ᱿") and bstack1111l11l1l_opy_(env.get(bstack1lllll1l_opy_ (u"ࠤࡇࡖࡔࡔࡅࠣᲀ"))):
        return {
            bstack1lllll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᲁ"): bstack1lllll1l_opy_ (u"ࠦࡉࡸ࡯࡯ࡧࠥᲂ"),
            bstack1lllll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᲃ"): env.get(bstack1lllll1l_opy_ (u"ࠨࡄࡓࡑࡑࡉࡤࡈࡕࡊࡎࡇࡣࡑࡏࡎࡌࠤᲄ")),
            bstack1lllll1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᲅ"): None,
            bstack1lllll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᲆ"): env.get(bstack1lllll1l_opy_ (u"ࠤࡇࡖࡔࡔࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᲇ"))
        }
    if env.get(bstack1lllll1l_opy_ (u"ࠥࡇࡎࠨᲈ")) == bstack1lllll1l_opy_ (u"ࠦࡹࡸࡵࡦࠤᲉ") and bstack1111l11l1l_opy_(env.get(bstack1lllll1l_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࠣᲊ"))):
        return {
            bstack1lllll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᲋"): bstack1lllll1l_opy_ (u"ࠢࡔࡧࡰࡥࡵ࡮࡯ࡳࡧࠥ᲌"),
            bstack1lllll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᲍"): env.get(bstack1lllll1l_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࡤࡕࡒࡈࡃࡑࡍ࡟ࡇࡔࡊࡑࡑࡣ࡚ࡘࡌࠣ᲎")),
            bstack1lllll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᲏"): env.get(bstack1lllll1l_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᲐ")),
            bstack1lllll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᲑ"): env.get(bstack1lllll1l_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡍࡓࡇࡥࡉࡅࠤᲒ"))
        }
    if env.get(bstack1lllll1l_opy_ (u"ࠢࡄࡋࠥᲓ")) == bstack1lllll1l_opy_ (u"ࠣࡶࡵࡹࡪࠨᲔ") and bstack1111l11l1l_opy_(env.get(bstack1lllll1l_opy_ (u"ࠤࡊࡍ࡙ࡒࡁࡃࡡࡆࡍࠧᲕ"))):
        return {
            bstack1lllll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᲖ"): bstack1lllll1l_opy_ (u"ࠦࡌ࡯ࡴࡍࡣࡥࠦᲗ"),
            bstack1lllll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᲘ"): env.get(bstack1lllll1l_opy_ (u"ࠨࡃࡊࡡࡍࡓࡇࡥࡕࡓࡎࠥᲙ")),
            bstack1lllll1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᲚ"): env.get(bstack1lllll1l_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᲛ")),
            bstack1lllll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲜ"): env.get(bstack1lllll1l_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢࡍࡉࠨᲝ"))
        }
    if env.get(bstack1lllll1l_opy_ (u"ࠦࡈࡏࠢᲞ")) == bstack1lllll1l_opy_ (u"ࠧࡺࡲࡶࡧࠥᲟ") and bstack1111l11l1l_opy_(env.get(bstack1lllll1l_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࠤᲠ"))):
        return {
            bstack1lllll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲡ"): bstack1lllll1l_opy_ (u"ࠣࡄࡸ࡭ࡱࡪ࡫ࡪࡶࡨࠦᲢ"),
            bstack1lllll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲣ"): env.get(bstack1lllll1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᲤ")),
            bstack1lllll1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲥ"): env.get(bstack1lllll1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡎࡄࡆࡊࡒࠢᲦ")) or env.get(bstack1lllll1l_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡓࡇࡍࡆࠤᲧ")),
            bstack1lllll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᲨ"): env.get(bstack1lllll1l_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᲩ"))
        }
    if bstack1111l11l1l_opy_(env.get(bstack1lllll1l_opy_ (u"ࠤࡗࡊࡤࡈࡕࡊࡎࡇࠦᲪ"))):
        return {
            bstack1lllll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᲫ"): bstack1lllll1l_opy_ (u"࡛ࠦ࡯ࡳࡶࡣ࡯ࠤࡘࡺࡵࡥ࡫ࡲࠤ࡙࡫ࡡ࡮ࠢࡖࡩࡷࡼࡩࡤࡧࡶࠦᲬ"),
            bstack1lllll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᲭ"): bstack1lllll1l_opy_ (u"ࠨࡻࡾࡽࢀࠦᲮ").format(env.get(bstack1lllll1l_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡋࡕࡕࡏࡆࡄࡘࡎࡕࡎࡔࡇࡕ࡚ࡊࡘࡕࡓࡋࠪᲯ")), env.get(bstack1lllll1l_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡖࡒࡐࡌࡈࡇ࡙ࡏࡄࠨᲰ"))),
            bstack1lllll1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᲱ"): env.get(bstack1lllll1l_opy_ (u"ࠥࡗ࡞࡙ࡔࡆࡏࡢࡈࡊࡌࡉࡏࡋࡗࡍࡔࡔࡉࡅࠤᲲ")),
            bstack1lllll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᲳ"): env.get(bstack1lllll1l_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧᲴ"))
        }
    if bstack1111l11l1l_opy_(env.get(bstack1lllll1l_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࠣᲵ"))):
        return {
            bstack1lllll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᲶ"): bstack1lllll1l_opy_ (u"ࠣࡃࡳࡴࡻ࡫ࡹࡰࡴࠥᲷ"),
            bstack1lllll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᲸ"): bstack1lllll1l_opy_ (u"ࠥࡿࢂ࠵ࡰࡳࡱ࡭ࡩࡨࡺ࠯ࡼࡿ࠲ࡿࢂ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾࠤᲹ").format(env.get(bstack1lllll1l_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡕࡓࡎࠪᲺ")), env.get(bstack1lllll1l_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡂࡅࡆࡓ࡚ࡔࡔࡠࡐࡄࡑࡊ࠭᲻")), env.get(bstack1lllll1l_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡒࡕࡓࡏࡋࡃࡕࡡࡖࡐ࡚ࡍࠧ᲼")), env.get(bstack1lllll1l_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫᲽ"))),
            bstack1lllll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲾ"): env.get(bstack1lllll1l_opy_ (u"ࠤࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᲿ")),
            bstack1lllll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳀"): env.get(bstack1lllll1l_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧ᳁"))
        }
    if env.get(bstack1lllll1l_opy_ (u"ࠧࡇ࡚ࡖࡔࡈࡣࡍ࡚ࡔࡑࡡࡘࡗࡊࡘ࡟ࡂࡉࡈࡒ࡙ࠨ᳂")) and env.get(bstack1lllll1l_opy_ (u"ࠨࡔࡇࡡࡅ࡙ࡎࡒࡄࠣ᳃")):
        return {
            bstack1lllll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᳄"): bstack1lllll1l_opy_ (u"ࠣࡃࡽࡹࡷ࡫ࠠࡄࡋࠥ᳅"),
            bstack1lllll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᳆"): bstack1lllll1l_opy_ (u"ࠥࡿࢂࢁࡽ࠰ࡡࡥࡹ࡮ࡲࡤ࠰ࡴࡨࡷࡺࡲࡴࡴࡁࡥࡹ࡮ࡲࡤࡊࡦࡀࡿࢂࠨ᳇").format(env.get(bstack1lllll1l_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡈࡒ࡙ࡓࡊࡁࡕࡋࡒࡒࡘࡋࡒࡗࡇࡕ࡙ࡗࡏࠧ᳈")), env.get(bstack1lllll1l_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡓࡖࡔࡐࡅࡄࡖࠪ᳉")), env.get(bstack1lllll1l_opy_ (u"࠭ࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉ࠭᳊"))),
            bstack1lllll1l_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᳋"): env.get(bstack1lllll1l_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠣ᳌")),
            bstack1lllll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ᳍"): env.get(bstack1lllll1l_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠥ᳎"))
        }
    if any([env.get(bstack1lllll1l_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤ᳏")), env.get(bstack1lllll1l_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡔࡈࡗࡔࡒࡖࡆࡆࡢࡗࡔ࡛ࡒࡄࡇࡢ࡚ࡊࡘࡓࡊࡑࡑࠦ᳐")), env.get(bstack1lllll1l_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡖࡓ࡚ࡘࡃࡆࡡ࡙ࡉࡗ࡙ࡉࡐࡐࠥ᳑"))]):
        return {
            bstack1lllll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᳒"): bstack1lllll1l_opy_ (u"ࠣࡃ࡚ࡗࠥࡉ࡯ࡥࡧࡅࡹ࡮ࡲࡤࠣ᳓"),
            bstack1lllll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰ᳔ࠧ"): env.get(bstack1lllll1l_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡐࡖࡄࡏࡍࡈࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤ᳕")),
            bstack1lllll1l_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳖"): env.get(bstack1lllll1l_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆ᳗ࠥ")),
            bstack1lllll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶ᳘ࠧ"): env.get(bstack1lllll1l_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈ᳙ࠧ"))
        }
    if env.get(bstack1lllll1l_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡤࡸ࡭ࡱࡪࡎࡶ࡯ࡥࡩࡷࠨ᳚")):
        return {
            bstack1lllll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᳛"): bstack1lllll1l_opy_ (u"ࠥࡆࡦࡳࡢࡰࡱ᳜ࠥ"),
            bstack1lllll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲ᳝ࠢ"): env.get(bstack1lllll1l_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡖࡪࡹࡵ࡭ࡶࡶ࡙ࡷࡲ᳞ࠢ")),
            bstack1lllll1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥ᳟ࠣ"): env.get(bstack1lllll1l_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡴࡪࡲࡶࡹࡐ࡯ࡣࡐࡤࡱࡪࠨ᳠")),
            bstack1lllll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᳡"): env.get(bstack1lllll1l_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡏࡷࡰࡦࡪࡸ᳢ࠢ"))
        }
    if env.get(bstack1lllll1l_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕ᳣ࠦ")) or env.get(bstack1lllll1l_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡓࡁࡊࡐࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤ࡙ࡔࡂࡔࡗࡉࡉࠨ᳤")):
        return {
            bstack1lllll1l_opy_ (u"ࠧࡴࡡ࡮ࡧ᳥ࠥ"): bstack1lllll1l_opy_ (u"ࠨࡗࡦࡴࡦ࡯ࡪࡸ᳦ࠢ"),
            bstack1lllll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮᳧ࠥ"): env.get(bstack1lllll1l_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐ᳨ࠧ")),
            bstack1lllll1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᳩ"): bstack1lllll1l_opy_ (u"ࠥࡑࡦ࡯࡮ࠡࡒ࡬ࡴࡪࡲࡩ࡯ࡧࠥᳪ") if env.get(bstack1lllll1l_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡓࡁࡊࡐࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤ࡙ࡔࡂࡔࡗࡉࡉࠨᳫ")) else None,
            bstack1lllll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᳬ"): env.get(bstack1lllll1l_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡈࡋࡗࡣࡈࡕࡍࡎࡋࡗ᳭ࠦ"))
        }
    if any([env.get(bstack1lllll1l_opy_ (u"ࠢࡈࡅࡓࡣࡕࡘࡏࡋࡇࡆࡘࠧᳮ")), env.get(bstack1lllll1l_opy_ (u"ࠣࡉࡆࡐࡔ࡛ࡄࡠࡒࡕࡓࡏࡋࡃࡕࠤᳯ")), env.get(bstack1lllll1l_opy_ (u"ࠤࡊࡓࡔࡍࡌࡆࡡࡆࡐࡔ࡛ࡄࡠࡒࡕࡓࡏࡋࡃࡕࠤᳰ"))]):
        return {
            bstack1lllll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᳱ"): bstack1lllll1l_opy_ (u"ࠦࡌࡵ࡯ࡨ࡮ࡨࠤࡈࡲ࡯ࡶࡦࠥᳲ"),
            bstack1lllll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᳳ"): None,
            bstack1lllll1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᳴"): env.get(bstack1lllll1l_opy_ (u"ࠢࡑࡔࡒࡎࡊࡉࡔࡠࡋࡇࠦᳵ")),
            bstack1lllll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᳶ"): env.get(bstack1lllll1l_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡋࡇࠦ᳷"))
        }
    if env.get(bstack1lllll1l_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࠨ᳸")):
        return {
            bstack1lllll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᳹"): bstack1lllll1l_opy_ (u"࡙ࠧࡨࡪࡲࡳࡥࡧࡲࡥࠣᳺ"),
            bstack1lllll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᳻"): env.get(bstack1lllll1l_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨ᳼")),
            bstack1lllll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᳽"): bstack1lllll1l_opy_ (u"ࠤࡍࡳࡧࠦࠣࡼࡿࠥ᳾").format(env.get(bstack1lllll1l_opy_ (u"ࠪࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡊࡐࡄࡢࡍࡉ࠭᳿"))) if env.get(bstack1lllll1l_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡋࡑࡅࡣࡎࡊࠢᴀ")) else None,
            bstack1lllll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴁ"): env.get(bstack1lllll1l_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᴂ"))
        }
    if bstack1111l11l1l_opy_(env.get(bstack1lllll1l_opy_ (u"ࠢࡏࡇࡗࡐࡎࡌ࡙ࠣᴃ"))):
        return {
            bstack1lllll1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᴄ"): bstack1lllll1l_opy_ (u"ࠤࡑࡩࡹࡲࡩࡧࡻࠥᴅ"),
            bstack1lllll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᴆ"): env.get(bstack1lllll1l_opy_ (u"ࠦࡉࡋࡐࡍࡑ࡜ࡣ࡚ࡘࡌࠣᴇ")),
            bstack1lllll1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴈ"): env.get(bstack1lllll1l_opy_ (u"ࠨࡓࡊࡖࡈࡣࡓࡇࡍࡆࠤᴉ")),
            bstack1lllll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴊ"): env.get(bstack1lllll1l_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᴋ"))
        }
    if bstack1111l11l1l_opy_(env.get(bstack1lllll1l_opy_ (u"ࠤࡊࡍ࡙ࡎࡕࡃࡡࡄࡇ࡙ࡏࡏࡏࡕࠥᴌ"))):
        return {
            bstack1lllll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᴍ"): bstack1lllll1l_opy_ (u"ࠦࡌ࡯ࡴࡉࡷࡥࠤࡆࡩࡴࡪࡱࡱࡷࠧᴎ"),
            bstack1lllll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᴏ"): bstack1lllll1l_opy_ (u"ࠨࡻࡾ࠱ࡾࢁ࠴ࡧࡣࡵ࡫ࡲࡲࡸ࠵ࡲࡶࡰࡶ࠳ࢀࢃࠢᴐ").format(env.get(bstack1lllll1l_opy_ (u"ࠧࡈࡋࡗࡌ࡚ࡈ࡟ࡔࡇࡕ࡚ࡊࡘ࡟ࡖࡔࡏࠫᴑ")), env.get(bstack1lllll1l_opy_ (u"ࠨࡉࡌࡘࡍ࡛ࡂࡠࡔࡈࡔࡔ࡙ࡉࡕࡑࡕ࡝ࠬᴒ")), env.get(bstack1lllll1l_opy_ (u"ࠩࡊࡍ࡙ࡎࡕࡃࡡࡕ࡙ࡓࡥࡉࡅࠩᴓ"))),
            bstack1lllll1l_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴔ"): env.get(bstack1lllll1l_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣ࡜ࡕࡒࡌࡈࡏࡓ࡜ࠨᴕ")),
            bstack1lllll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴖ"): env.get(bstack1lllll1l_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡒࡖࡐࡢࡍࡉࠨᴗ"))
        }
    if env.get(bstack1lllll1l_opy_ (u"ࠢࡄࡋࠥᴘ")) == bstack1lllll1l_opy_ (u"ࠣࡶࡵࡹࡪࠨᴙ") and env.get(bstack1lllll1l_opy_ (u"ࠤ࡙ࡉࡗࡉࡅࡍࠤᴚ")) == bstack1lllll1l_opy_ (u"ࠥ࠵ࠧᴛ"):
        return {
            bstack1lllll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᴜ"): bstack1lllll1l_opy_ (u"ࠧ࡜ࡥࡳࡥࡨࡰࠧᴝ"),
            bstack1lllll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᴞ"): bstack1lllll1l_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࡼࡿࠥᴟ").format(env.get(bstack1lllll1l_opy_ (u"ࠨࡘࡈࡖࡈࡋࡌࡠࡗࡕࡐࠬᴠ"))),
            bstack1lllll1l_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᴡ"): None,
            bstack1lllll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᴢ"): None,
        }
    if env.get(bstack1lllll1l_opy_ (u"࡙ࠦࡋࡁࡎࡅࡌࡘ࡞ࡥࡖࡆࡔࡖࡍࡔࡔࠢᴣ")):
        return {
            bstack1lllll1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴤ"): bstack1lllll1l_opy_ (u"ࠨࡔࡦࡣࡰࡧ࡮ࡺࡹࠣᴥ"),
            bstack1lllll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴦ"): None,
            bstack1lllll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᴧ"): env.get(bstack1lllll1l_opy_ (u"ࠤࡗࡉࡆࡓࡃࡊࡖ࡜ࡣࡕࡘࡏࡋࡇࡆࡘࡤࡔࡁࡎࡇࠥᴨ")),
            bstack1lllll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᴩ"): env.get(bstack1lllll1l_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᴪ"))
        }
    if any([env.get(bstack1lllll1l_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࠣᴫ")), env.get(bstack1lllll1l_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࡡࡘࡖࡑࠨᴬ")), env.get(bstack1lllll1l_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠧᴭ")), env.get(bstack1lllll1l_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࡣ࡙ࡋࡁࡎࠤᴮ"))]):
        return {
            bstack1lllll1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᴯ"): bstack1lllll1l_opy_ (u"ࠥࡇࡴࡴࡣࡰࡷࡵࡷࡪࠨᴰ"),
            bstack1lllll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᴱ"): None,
            bstack1lllll1l_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᴲ"): env.get(bstack1lllll1l_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᴳ")) or None,
            bstack1lllll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴴ"): env.get(bstack1lllll1l_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᴵ"), 0)
        }
    if env.get(bstack1lllll1l_opy_ (u"ࠤࡊࡓࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᴶ")):
        return {
            bstack1lllll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣᴷ"): bstack1lllll1l_opy_ (u"ࠦࡌࡵࡃࡅࠤᴸ"),
            bstack1lllll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᴹ"): None,
            bstack1lllll1l_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᴺ"): env.get(bstack1lllll1l_opy_ (u"ࠢࡈࡑࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᴻ")),
            bstack1lllll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᴼ"): env.get(bstack1lllll1l_opy_ (u"ࠤࡊࡓࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡄࡑࡘࡒ࡙ࡋࡒࠣᴽ"))
        }
    if env.get(bstack1lllll1l_opy_ (u"ࠥࡇࡋࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣᴾ")):
        return {
            bstack1lllll1l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᴿ"): bstack1lllll1l_opy_ (u"ࠧࡉ࡯ࡥࡧࡉࡶࡪࡹࡨࠣᵀ"),
            bstack1lllll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᵁ"): env.get(bstack1lllll1l_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᵂ")),
            bstack1lllll1l_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᵃ"): env.get(bstack1lllll1l_opy_ (u"ࠤࡆࡊࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡏࡃࡐࡉࠧᵄ")),
            bstack1lllll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᵅ"): env.get(bstack1lllll1l_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤᵆ"))
        }
    return {bstack1lllll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᵇ"): None}
def get_host_info():
    return {
        bstack1lllll1l_opy_ (u"ࠨࡨࡰࡵࡷࡲࡦࡳࡥࠣᵈ"): platform.node(),
        bstack1lllll1l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠤᵉ"): platform.system(),
        bstack1lllll1l_opy_ (u"ࠣࡶࡼࡴࡪࠨᵊ"): platform.machine(),
        bstack1lllll1l_opy_ (u"ࠤࡹࡩࡷࡹࡩࡰࡰࠥᵋ"): platform.version(),
        bstack1lllll1l_opy_ (u"ࠥࡥࡷࡩࡨࠣᵌ"): platform.architecture()[0]
    }
def bstack111ll1111l_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111l11lllll_opy_():
    if bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬᵍ")):
        return bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᵎ")
    return bstack1lllll1l_opy_ (u"࠭ࡵ࡯࡭ࡱࡳࡼࡴ࡟ࡨࡴ࡬ࡨࠬᵏ")
def bstack1111lll1ll1_opy_(driver):
    info = {
        bstack1lllll1l_opy_ (u"ࠧࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ᵐ"): driver.capabilities,
        bstack1lllll1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠬᵑ"): driver.session_id,
        bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪᵒ"): driver.capabilities.get(bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨᵓ"), None),
        bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᵔ"): driver.capabilities.get(bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᵕ"), None),
        bstack1lllll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠨᵖ"): driver.capabilities.get(bstack1lllll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭ᵗ"), None),
        bstack1lllll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫᵘ"):driver.capabilities.get(bstack1lllll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫᵙ"), None),
    }
    if bstack111l11lllll_opy_() == bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᵚ"):
        if bstack1l1l111l11_opy_():
            info[bstack1lllll1l_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬᵛ")] = bstack1lllll1l_opy_ (u"ࠬࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᵜ")
        elif driver.capabilities.get(bstack1lllll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᵝ"), {}).get(bstack1lllll1l_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫᵞ"), False):
            info[bstack1lllll1l_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩᵟ")] = bstack1lllll1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ᵠ")
        else:
            info[bstack1lllll1l_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫᵡ")] = bstack1lllll1l_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᵢ")
    return info
def bstack1l1l111l11_opy_():
    if bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠬࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠫᵣ")):
        return True
    if bstack1111l11l1l_opy_(os.environ.get(bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧᵤ"), None)):
        return True
    return False
def bstack11l1l111l1_opy_(bstack1111lll1111_opy_, url, data, config):
    headers = config.get(bstack1lllll1l_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨᵥ"), None)
    proxies = bstack1ll111lll_opy_(config, url)
    auth = config.get(bstack1lllll1l_opy_ (u"ࠨࡣࡸࡸ࡭࠭ᵦ"), None)
    response = requests.request(
            bstack1111lll1111_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1llll1111l_opy_(bstack11ll1l1111_opy_, size):
    bstack1111ll111l_opy_ = []
    while len(bstack11ll1l1111_opy_) > size:
        bstack1ll1l1l11l_opy_ = bstack11ll1l1111_opy_[:size]
        bstack1111ll111l_opy_.append(bstack1ll1l1l11l_opy_)
        bstack11ll1l1111_opy_ = bstack11ll1l1111_opy_[size:]
    bstack1111ll111l_opy_.append(bstack11ll1l1111_opy_)
    return bstack1111ll111l_opy_
def bstack111l1lll1l1_opy_(message, bstack111l1lll1ll_opy_=False):
    os.write(1, bytes(message, bstack1lllll1l_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᵧ")))
    os.write(1, bytes(bstack1lllll1l_opy_ (u"ࠪࡠࡳ࠭ᵨ"), bstack1lllll1l_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᵩ")))
    if bstack111l1lll1ll_opy_:
        with open(bstack1lllll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠲ࡵ࠱࠲ࡻ࠰ࠫᵪ") + os.environ[bstack1lllll1l_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬᵫ")] + bstack1lllll1l_opy_ (u"ࠧ࠯࡮ࡲ࡫ࠬᵬ"), bstack1lllll1l_opy_ (u"ࠨࡣࠪᵭ")) as f:
            f.write(message + bstack1lllll1l_opy_ (u"ࠩ࡟ࡲࠬᵮ"))
def bstack1lll1ll11ll_opy_():
    return os.environ[bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ᵯ")].lower() == bstack1lllll1l_opy_ (u"ࠫࡹࡸࡵࡦࠩᵰ")
def bstack1l1111ll_opy_():
    return bstack1l111ll1_opy_().replace(tzinfo=None).isoformat() + bstack1lllll1l_opy_ (u"ࠬࡠࠧᵱ")
def bstack111l11ll1l1_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack1lllll1l_opy_ (u"࡚࠭ࠨᵲ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack1lllll1l_opy_ (u"࡛ࠧࠩᵳ")))).total_seconds() * 1000
def bstack1111ll1llll_opy_(timestamp):
    return bstack1111l111lll_opy_(timestamp).isoformat() + bstack1lllll1l_opy_ (u"ࠨ࡜ࠪᵴ")
def bstack1111llll1l1_opy_(bstack1111llll111_opy_):
    date_format = bstack1lllll1l_opy_ (u"ࠩࠨ࡝ࠪࡳࠥࡥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖ࠲ࠪ࡬ࠧᵵ")
    bstack1111llllll1_opy_ = datetime.datetime.strptime(bstack1111llll111_opy_, date_format)
    return bstack1111llllll1_opy_.isoformat() + bstack1lllll1l_opy_ (u"ࠪ࡞ࠬᵶ")
def bstack1111l11l1l1_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack1lllll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᵷ")
    else:
        return bstack1lllll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᵸ")
def bstack1111l11l1l_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack1lllll1l_opy_ (u"࠭ࡴࡳࡷࡨࠫᵹ")
def bstack111l111ll1l_opy_(val):
    return val.__str__().lower() == bstack1lllll1l_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ᵺ")
def error_handler(bstack1111l11l111_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1111l11l111_opy_ as e:
                print(bstack1lllll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡾࢁࠥ࠳࠾ࠡࡽࢀ࠾ࠥࢁࡽࠣᵻ").format(func.__name__, bstack1111l11l111_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1111ll1ll11_opy_(bstack111l11l111l_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack111l11l111l_opy_(cls, *args, **kwargs)
            except bstack1111l11l111_opy_ as e:
                print(bstack1lllll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡿࢂࠦ࠭࠿ࠢࡾࢁ࠿ࠦࡻࡾࠤᵼ").format(bstack111l11l111l_opy_.__name__, bstack1111l11l111_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1111ll1ll11_opy_
    else:
        return decorator
def bstack111l1lll11_opy_(bstack1lll111l1_opy_):
    if os.getenv(bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ᵽ")) is not None:
        return bstack1111l11l1l_opy_(os.getenv(bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧᵾ")))
    if bstack1lllll1l_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᵿ") in bstack1lll111l1_opy_ and bstack111l111ll1l_opy_(bstack1lll111l1_opy_[bstack1lllll1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᶀ")]):
        return False
    if bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᶁ") in bstack1lll111l1_opy_ and bstack111l111ll1l_opy_(bstack1lll111l1_opy_[bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᶂ")]):
        return False
    return True
def bstack11l1ll11l1_opy_():
    try:
        from pytest_bdd import reporting
        bstack111l1111111_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡗࡖࡉࡗࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠤᶃ"), None)
        return bstack111l1111111_opy_ is None or bstack111l1111111_opy_ == bstack1lllll1l_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠢᶄ")
    except Exception as e:
        return False
def bstack11l1l11lll_opy_(hub_url, CONFIG):
    if bstack1l111llll1_opy_() <= version.parse(bstack1lllll1l_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫᶅ")):
        if hub_url:
            return bstack1lllll1l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨᶆ") + hub_url + bstack1lllll1l_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥᶇ")
        return bstack1ll111111l_opy_
    if hub_url:
        return bstack1lllll1l_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤᶈ") + hub_url + bstack1lllll1l_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤᶉ")
    return bstack111lll11l1_opy_
def bstack111l1111ll1_opy_():
    return isinstance(os.getenv(bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡏ࡙ࡌࡏࡎࠨᶊ")), str)
def bstack111lll1l1_opy_(url):
    return urlparse(url).hostname
def bstack11l11l1l11_opy_(hostname):
    for bstack1lll1lllll_opy_ in bstack1lll1l1ll1_opy_:
        regex = re.compile(bstack1lll1lllll_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll1111ll1_opy_(bstack111l111llll_opy_, file_name, logger):
    bstack1l11l1ll11_opy_ = os.path.join(os.path.expanduser(bstack1lllll1l_opy_ (u"ࠪࢂࠬᶋ")), bstack111l111llll_opy_)
    try:
        if not os.path.exists(bstack1l11l1ll11_opy_):
            os.makedirs(bstack1l11l1ll11_opy_)
        file_path = os.path.join(os.path.expanduser(bstack1lllll1l_opy_ (u"ࠫࢃ࠭ᶌ")), bstack111l111llll_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack1lllll1l_opy_ (u"ࠬࡽࠧᶍ")):
                pass
            with open(file_path, bstack1lllll1l_opy_ (u"ࠨࡷࠬࠤᶎ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1lll11l1ll_opy_.format(str(e)))
def bstack11ll1111lll_opy_(file_name, key, value, logger):
    file_path = bstack11ll1111ll1_opy_(bstack1lllll1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᶏ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1lll1l11ll_opy_ = json.load(open(file_path, bstack1lllll1l_opy_ (u"ࠨࡴࡥࠫᶐ")))
        else:
            bstack1lll1l11ll_opy_ = {}
        bstack1lll1l11ll_opy_[key] = value
        with open(file_path, bstack1lllll1l_opy_ (u"ࠤࡺ࠯ࠧᶑ")) as outfile:
            json.dump(bstack1lll1l11ll_opy_, outfile)
def bstack1l1l11l1l1_opy_(file_name, logger):
    file_path = bstack11ll1111ll1_opy_(bstack1lllll1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᶒ"), file_name, logger)
    bstack1lll1l11ll_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack1lllll1l_opy_ (u"ࠫࡷ࠭ᶓ")) as bstack1ll11ll11_opy_:
            bstack1lll1l11ll_opy_ = json.load(bstack1ll11ll11_opy_)
    return bstack1lll1l11ll_opy_
def bstack1l1l1l1l11_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack1lllll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡥࡧ࡯ࡩࡹ࡯࡮ࡨࠢࡩ࡭ࡱ࡫࠺ࠡࠩᶔ") + file_path + bstack1lllll1l_opy_ (u"࠭ࠠࠨᶕ") + str(e))
def bstack1l111llll1_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack1lllll1l_opy_ (u"ࠢ࠽ࡐࡒࡘࡘࡋࡔ࠿ࠤᶖ")
def bstack111ll1l11_opy_(config):
    if bstack1lllll1l_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᶗ") in config:
        del (config[bstack1lllll1l_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᶘ")])
        return False
    if bstack1l111llll1_opy_() < version.parse(bstack1lllll1l_opy_ (u"ࠪ࠷࠳࠺࠮࠱ࠩᶙ")):
        return False
    if bstack1l111llll1_opy_() >= version.parse(bstack1lllll1l_opy_ (u"ࠫ࠹࠴࠱࠯࠷ࠪᶚ")):
        return True
    if bstack1lllll1l_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬᶛ") in config and config[bstack1lllll1l_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ᶜ")] is False:
        return False
    else:
        return True
def bstack111ll1l111_opy_(args_list, bstack111l11llll1_opy_):
    index = -1
    for value in bstack111l11llll1_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack1111l1llll1_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack1111l1llll1_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1lll11l1_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1lll11l1_opy_ = bstack1lll11l1_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack1lllll1l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᶝ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack1lllll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᶞ"), exception=exception)
    def bstack111111l111_opy_(self):
        if self.result != bstack1lllll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᶟ"):
            return None
        if isinstance(self.exception_type, str) and bstack1lllll1l_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨᶠ") in self.exception_type:
            return bstack1lllll1l_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧᶡ")
        return bstack1lllll1l_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨᶢ")
    def bstack1111l1lll11_opy_(self):
        if self.result != bstack1lllll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᶣ"):
            return None
        if self.bstack1lll11l1_opy_:
            return self.bstack1lll11l1_opy_
        return bstack1111lll11l1_opy_(self.exception)
def bstack1111lll11l1_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111l111l1l1_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l11l1l1_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1ll1111ll_opy_(config, logger):
    try:
        import playwright
        bstack111l1ll11ll_opy_ = playwright.__file__
        bstack1111ll1l111_opy_ = os.path.split(bstack111l1ll11ll_opy_)
        bstack111l11l1111_opy_ = bstack1111ll1l111_opy_[0] + bstack1lllll1l_opy_ (u"ࠧ࠰ࡦࡵ࡭ࡻ࡫ࡲ࠰ࡲࡤࡧࡰࡧࡧࡦ࠱࡯࡭ࡧ࠵ࡣ࡭࡫࠲ࡧࡱ࡯࠮࡫ࡵࠪᶤ")
        os.environ[bstack1lllll1l_opy_ (u"ࠨࡉࡏࡓࡇࡇࡌࡠࡃࡊࡉࡓ࡚࡟ࡉࡖࡗࡔࡤࡖࡒࡐ࡚࡜ࠫᶥ")] = bstack111l11ll1_opy_(config)
        with open(bstack111l11l1111_opy_, bstack1lllll1l_opy_ (u"ࠩࡵࠫᶦ")) as f:
            file_content = f.read()
            bstack111l11l1l11_opy_ = bstack1lllll1l_opy_ (u"ࠪ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠩᶧ")
            bstack111l1l1ll1l_opy_ = file_content.find(bstack111l11l1l11_opy_)
            if bstack111l1l1ll1l_opy_ == -1:
              process = subprocess.Popen(bstack1lllll1l_opy_ (u"ࠦࡳࡶ࡭ࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡪࡰࡴࡨࡡ࡭࠯ࡤ࡫ࡪࡴࡴࠣᶨ"), shell=True, cwd=bstack1111ll1l111_opy_[0])
              process.wait()
              bstack111l1111lll_opy_ = bstack1lllll1l_opy_ (u"ࠬࠨࡵࡴࡧࠣࡷࡹࡸࡩࡤࡶࠥ࠿ࠬᶩ")
              bstack1111lllllll_opy_ = bstack1lllll1l_opy_ (u"ࠨࠢࠣࠢ࡟ࠦࡺࡹࡥࠡࡵࡷࡶ࡮ࡩࡴ࡝ࠤ࠾ࠤࡨࡵ࡮ࡴࡶࠣࡿࠥࡨ࡯ࡰࡶࡶࡸࡷࡧࡰࠡࡿࠣࡁࠥࡸࡥࡲࡷ࡬ࡶࡪ࠮ࠧࡨ࡮ࡲࡦࡦࡲ࠭ࡢࡩࡨࡲࡹ࠭ࠩ࠼ࠢ࡬ࡪࠥ࠮ࡰࡳࡱࡦࡩࡸࡹ࠮ࡦࡰࡹ࠲ࡌࡒࡏࡃࡃࡏࡣࡆࡍࡅࡏࡖࡢࡌ࡙࡚ࡐࡠࡒࡕࡓ࡝࡟ࠩࠡࡤࡲࡳࡹࡹࡴࡳࡣࡳࠬ࠮ࡁࠠࠣࠤࠥᶪ")
              bstack1111l1lll1l_opy_ = file_content.replace(bstack111l1111lll_opy_, bstack1111lllllll_opy_)
              with open(bstack111l11l1111_opy_, bstack1lllll1l_opy_ (u"ࠧࡸࠩᶫ")) as f:
                f.write(bstack1111l1lll1l_opy_)
    except Exception as e:
        logger.error(bstack11lll11l1_opy_.format(str(e)))
def bstack1ll1l11ll1_opy_():
  try:
    bstack1111l1lllll_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡳࡡ࡭ࡡ࡫ࡹࡧࡥࡵࡳ࡮࠱࡮ࡸࡵ࡮ࠨᶬ"))
    bstack111l11ll1ll_opy_ = []
    if os.path.exists(bstack1111l1lllll_opy_):
      with open(bstack1111l1lllll_opy_) as f:
        bstack111l11ll1ll_opy_ = json.load(f)
      os.remove(bstack1111l1lllll_opy_)
    return bstack111l11ll1ll_opy_
  except:
    pass
  return []
def bstack1l11ll111l_opy_(bstack1llll11l1l_opy_):
  try:
    bstack111l11ll1ll_opy_ = []
    bstack1111l1lllll_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1l_opy_ (u"ࠩࡲࡴࡹ࡯࡭ࡢ࡮ࡢ࡬ࡺࡨ࡟ࡶࡴ࡯࠲࡯ࡹ࡯࡯ࠩᶭ"))
    if os.path.exists(bstack1111l1lllll_opy_):
      with open(bstack1111l1lllll_opy_) as f:
        bstack111l11ll1ll_opy_ = json.load(f)
    bstack111l11ll1ll_opy_.append(bstack1llll11l1l_opy_)
    with open(bstack1111l1lllll_opy_, bstack1lllll1l_opy_ (u"ࠪࡻࠬᶮ")) as f:
        json.dump(bstack111l11ll1ll_opy_, f)
  except:
    pass
def bstack111ll1lll_opy_(logger, bstack1111ll111ll_opy_ = False):
  try:
    test_name = os.environ.get(bstack1lllll1l_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗࡣ࡙ࡋࡓࡕࡡࡑࡅࡒࡋࠧᶯ"), bstack1lllll1l_opy_ (u"ࠬ࠭ᶰ"))
    if test_name == bstack1lllll1l_opy_ (u"࠭ࠧᶱ"):
        test_name = threading.current_thread().__dict__.get(bstack1lllll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࡂࡥࡦࡢࡸࡪࡹࡴࡠࡰࡤࡱࡪ࠭ᶲ"), bstack1lllll1l_opy_ (u"ࠨࠩᶳ"))
    bstack1111ll1ll1l_opy_ = bstack1lllll1l_opy_ (u"ࠩ࠯ࠤࠬᶴ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack1111ll111ll_opy_:
        bstack11ll1l1ll_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪᶵ"), bstack1lllll1l_opy_ (u"ࠫ࠵࠭ᶶ"))
        bstack1l1ll11l1l_opy_ = {bstack1lllll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᶷ"): test_name, bstack1lllll1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᶸ"): bstack1111ll1ll1l_opy_, bstack1lllll1l_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ᶹ"): bstack11ll1l1ll_opy_}
        bstack111l11ll11l_opy_ = []
        bstack1111llll11l_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡲࡳࡴࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧᶺ"))
        if os.path.exists(bstack1111llll11l_opy_):
            with open(bstack1111llll11l_opy_) as f:
                bstack111l11ll11l_opy_ = json.load(f)
        bstack111l11ll11l_opy_.append(bstack1l1ll11l1l_opy_)
        with open(bstack1111llll11l_opy_, bstack1lllll1l_opy_ (u"ࠩࡺࠫᶻ")) as f:
            json.dump(bstack111l11ll11l_opy_, f)
    else:
        bstack1l1ll11l1l_opy_ = {bstack1lllll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨᶼ"): test_name, bstack1lllll1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᶽ"): bstack1111ll1ll1l_opy_, bstack1lllll1l_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᶾ"): str(multiprocessing.current_process().name)}
        if bstack1lllll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶࠪᶿ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1l1ll11l1l_opy_)
  except Exception as e:
      logger.warn(bstack1lllll1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡳࡽࡹ࡫ࡳࡵࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧ࠺ࠡࡽࢀࠦ᷀").format(e))
def bstack1l1l11lll_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1lllll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠣࡲࡴࡺࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡦࡦࡹࡩࡤࠢࡩ࡭ࡱ࡫ࠠࡰࡲࡨࡶࡦࡺࡩࡰࡰࡶࠫ᷁"))
    try:
      bstack111l11lll11_opy_ = []
      bstack1l1ll11l1l_opy_ = {bstack1lllll1l_opy_ (u"ࠩࡱࡥࡲ࡫᷂ࠧ"): test_name, bstack1lllll1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ᷃"): error_message, bstack1lllll1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ᷄"): index}
      bstack111l1l1l111_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭᷅"))
      if os.path.exists(bstack111l1l1l111_opy_):
          with open(bstack111l1l1l111_opy_) as f:
              bstack111l11lll11_opy_ = json.load(f)
      bstack111l11lll11_opy_.append(bstack1l1ll11l1l_opy_)
      with open(bstack111l1l1l111_opy_, bstack1lllll1l_opy_ (u"࠭ࡷࠨ᷆")) as f:
          json.dump(bstack111l11lll11_opy_, f)
    except Exception as e:
      logger.warn(bstack1lllll1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡵࡳࡧࡵࡴࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥ᷇").format(e))
    return
  bstack111l11lll11_opy_ = []
  bstack1l1ll11l1l_opy_ = {bstack1lllll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭᷈"): test_name, bstack1lllll1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ᷉"): error_message, bstack1lllll1l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹ᷊ࠩ"): index}
  bstack111l1l1l111_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬ᷋"))
  lock_file = bstack111l1l1l111_opy_ + bstack1lllll1l_opy_ (u"ࠬ࠴࡬ࡰࡥ࡮ࠫ᷌")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack111l1l1l111_opy_):
          with open(bstack111l1l1l111_opy_, bstack1lllll1l_opy_ (u"࠭ࡲࠨ᷍")) as f:
              content = f.read().strip()
              if content:
                  bstack111l11lll11_opy_ = json.load(open(bstack111l1l1l111_opy_))
      bstack111l11lll11_opy_.append(bstack1l1ll11l1l_opy_)
      with open(bstack111l1l1l111_opy_, bstack1lllll1l_opy_ (u"ࠧࡸ᷎ࠩ")) as f:
          json.dump(bstack111l11lll11_opy_, f)
  except Exception as e:
    logger.warn(bstack1lllll1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡶࡴࡨ࡯ࡵࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡬ࡩ࡭ࡧࠣࡰࡴࡩ࡫ࡪࡰࡪ࠾ࠥࢁࡽ᷏ࠣ").format(e))
def bstack1l1l1llll_opy_(bstack1l11l11lll_opy_, name, logger):
  try:
    bstack1l1ll11l1l_opy_ = {bstack1lllll1l_opy_ (u"ࠩࡱࡥࡲ࡫᷐ࠧ"): name, bstack1lllll1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ᷑"): bstack1l11l11lll_opy_, bstack1lllll1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ᷒"): str(threading.current_thread()._name)}
    return bstack1l1ll11l1l_opy_
  except Exception as e:
    logger.warn(bstack1lllll1l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡧࡷࡱࡲࡪࡲࠠࡥࡣࡷࡥ࠿ࠦࡻࡾࠤᷓ").format(e))
  return
def bstack111l1ll1111_opy_():
    return platform.system() == bstack1lllll1l_opy_ (u"࠭ࡗࡪࡰࡧࡳࡼࡹࠧᷔ")
def bstack1l1lll111_opy_(bstack1111l1l1ll1_opy_, config, logger):
    bstack1111lll111l_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack1111l1l1ll1_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack1lllll1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪ࡮ࡲࡴࡦࡴࠣࡧࡴࡴࡦࡪࡩࠣ࡯ࡪࡿࡳࠡࡤࡼࠤࡷ࡫ࡧࡦࡺࠣࡱࡦࡺࡣࡩ࠼ࠣࡿࢂࠨᷕ").format(e))
    return bstack1111lll111l_opy_
def bstack11l1l1l1lll_opy_(bstack111l1ll1l1l_opy_, bstack111l1ll1l11_opy_):
    bstack111l1l1l11l_opy_ = version.parse(bstack111l1ll1l1l_opy_)
    bstack111l11lll1l_opy_ = version.parse(bstack111l1ll1l11_opy_)
    if bstack111l1l1l11l_opy_ > bstack111l11lll1l_opy_:
        return 1
    elif bstack111l1l1l11l_opy_ < bstack111l11lll1l_opy_:
        return -1
    else:
        return 0
def bstack1l111ll1_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack1111l111lll_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack111l1ll11l1_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack11ll1llll_opy_(options, framework, config, bstack111l1lll1l_opy_={}):
    if options is None:
        return
    if getattr(options, bstack1lllll1l_opy_ (u"ࠨࡩࡨࡸࠬᷖ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1lll1ll1ll_opy_ = caps.get(bstack1lllll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᷗ"))
    bstack111l1ll1ll1_opy_ = True
    bstack11l11111l1_opy_ = os.environ[bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᷘ")]
    bstack1l1111l1lll_opy_ = config.get(bstack1lllll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᷙ"), False)
    if bstack1l1111l1lll_opy_:
        bstack1l1l1l111ll_opy_ = config.get(bstack1lllll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᷚ"), {})
        bstack1l1l1l111ll_opy_[bstack1lllll1l_opy_ (u"࠭ࡡࡶࡶ࡫ࡘࡴࡱࡥ࡯ࠩᷛ")] = os.getenv(bstack1lllll1l_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬᷜ"))
        bstack111l1l1ll11_opy_ = json.loads(os.getenv(bstack1lllll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩᷝ"), bstack1lllll1l_opy_ (u"ࠩࡾࢁࠬᷞ"))).get(bstack1lllll1l_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᷟ"))
    if bstack111l111ll1l_opy_(caps.get(bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫ࡗ࠴ࡅࠪᷠ"))) or bstack111l111ll1l_opy_(caps.get(bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡠࡹ࠶ࡧࠬᷡ"))):
        bstack111l1ll1ll1_opy_ = False
    if bstack111ll1l11_opy_({bstack1lllll1l_opy_ (u"ࠨࡵࡴࡧ࡚࠷ࡈࠨᷢ"): bstack111l1ll1ll1_opy_}):
        bstack1lll1ll1ll_opy_ = bstack1lll1ll1ll_opy_ or {}
        bstack1lll1ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩᷣ")] = bstack111l1ll11l1_opy_(framework)
        bstack1lll1ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪᷤ")] = bstack1lll1ll11ll_opy_()
        bstack1lll1ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᷥ")] = bstack11l11111l1_opy_
        bstack1lll1ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬᷦ")] = bstack111l1lll1l_opy_
        if bstack1l1111l1lll_opy_:
            bstack1lll1ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᷧ")] = bstack1l1111l1lll_opy_
            bstack1lll1ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᷨ")] = bstack1l1l1l111ll_opy_
            bstack1lll1ll1ll_opy_[bstack1lllll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᷩ")][bstack1lllll1l_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᷪ")] = bstack111l1l1ll11_opy_
        if getattr(options, bstack1lllll1l_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩᷫ"), None):
            options.set_capability(bstack1lllll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᷬ"), bstack1lll1ll1ll_opy_)
        else:
            options[bstack1lllll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᷭ")] = bstack1lll1ll1ll_opy_
    else:
        if getattr(options, bstack1lllll1l_opy_ (u"ࠫࡸ࡫ࡴࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷࡽࠬᷮ"), None):
            options.set_capability(bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ᷯ"), bstack111l1ll11l1_opy_(framework))
            options.set_capability(bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧᷰ"), bstack1lll1ll11ll_opy_())
            options.set_capability(bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩᷱ"), bstack11l11111l1_opy_)
            options.set_capability(bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩᷲ"), bstack111l1lll1l_opy_)
            if bstack1l1111l1lll_opy_:
                options.set_capability(bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᷳ"), bstack1l1111l1lll_opy_)
                options.set_capability(bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᷴ"), bstack1l1l1l111ll_opy_)
                options.set_capability(bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵ࠱ࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ᷵"), bstack111l1l1ll11_opy_)
        else:
            options[bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭᷶")] = bstack111l1ll11l1_opy_(framework)
            options[bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ᷷ࠧ")] = bstack1lll1ll11ll_opy_()
            options[bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥ᷸ࠩ")] = bstack11l11111l1_opy_
            options[bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱ᷹ࠩ")] = bstack111l1lll1l_opy_
            if bstack1l1111l1lll_opy_:
                options[bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ᷺")] = bstack1l1111l1lll_opy_
                options[bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᷻")] = bstack1l1l1l111ll_opy_
                options[bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ᷼")][bstack1lllll1l_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ᷽࠭")] = bstack111l1l1ll11_opy_
    return options
def bstack1111lll1lll_opy_(ws_endpoint, framework):
    bstack111l1lll1l_opy_ = bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠨࡐࡍࡃ࡜࡛ࡗࡏࡇࡉࡖࡢࡔࡗࡕࡄࡖࡅࡗࡣࡒࡇࡐࠣ᷾"))
    if ws_endpoint and len(ws_endpoint.split(bstack1lllll1l_opy_ (u"ࠧࡤࡣࡳࡷࡂ᷿࠭"))) > 1:
        ws_url = ws_endpoint.split(bstack1lllll1l_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧḀ"))[0]
        if bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬḁ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack1111l1ll1ll_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack1lllll1l_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩḂ"))[1]))
            bstack1111l1ll1ll_opy_ = bstack1111l1ll1ll_opy_ or {}
            bstack11l11111l1_opy_ = os.environ[bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩḃ")]
            bstack1111l1ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭Ḅ")] = str(framework) + str(__version__)
            bstack1111l1ll1ll_opy_[bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧḅ")] = bstack1lll1ll11ll_opy_()
            bstack1111l1ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩḆ")] = bstack11l11111l1_opy_
            bstack1111l1ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩḇ")] = bstack111l1lll1l_opy_
            ws_endpoint = ws_endpoint.split(bstack1lllll1l_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨḈ"))[0] + bstack1lllll1l_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩḉ") + urllib.parse.quote(json.dumps(bstack1111l1ll1ll_opy_))
    return ws_endpoint
def bstack1ll11l1ll_opy_():
    global bstack111llllll1_opy_
    from playwright._impl._browser_type import BrowserType
    bstack111llllll1_opy_ = BrowserType.connect
    return bstack111llllll1_opy_
def bstack11ll1ll111_opy_(framework_name):
    global bstack1l11ll11l1_opy_
    bstack1l11ll11l1_opy_ = framework_name
    return framework_name
def bstack111l111ll_opy_(self, *args, **kwargs):
    global bstack111llllll1_opy_
    try:
        global bstack1l11ll11l1_opy_
        if bstack1lllll1l_opy_ (u"ࠫࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴࠨḊ") in kwargs:
            kwargs[bstack1lllll1l_opy_ (u"ࠬࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵࠩḋ")] = bstack1111lll1lll_opy_(
                kwargs.get(bstack1lllll1l_opy_ (u"࠭ࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶࠪḌ"), None),
                bstack1l11ll11l1_opy_
            )
    except Exception as e:
        logger.error(bstack1lllll1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩࡧࡱࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡕࡇࡏࠥࡩࡡࡱࡵ࠽ࠤࢀࢃࠢḍ").format(str(e)))
    return bstack111llllll1_opy_(self, *args, **kwargs)
def bstack1111l11lll1_opy_(bstack1111ll11l11_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1ll111lll_opy_(bstack1111ll11l11_opy_, bstack1lllll1l_opy_ (u"ࠣࠤḎ"))
        if proxies and proxies.get(bstack1lllll1l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳࠣḏ")):
            parsed_url = urlparse(proxies.get(bstack1lllll1l_opy_ (u"ࠥ࡬ࡹࡺࡰࡴࠤḐ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack1lllll1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡋࡳࡸࡺࠧḑ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack1lllll1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡴࡸࡴࠨḒ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack1lllll1l_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡚ࡹࡥࡳࠩḓ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack1lllll1l_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖࡡࡴࡵࠪḔ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1111lllll1_opy_(bstack1111ll11l11_opy_):
    bstack111l11l1ll1_opy_ = {
        bstack11l11lll111_opy_[bstack111l1lll111_opy_]: bstack1111ll11l11_opy_[bstack111l1lll111_opy_]
        for bstack111l1lll111_opy_ in bstack1111ll11l11_opy_
        if bstack111l1lll111_opy_ in bstack11l11lll111_opy_
    }
    bstack111l11l1ll1_opy_[bstack1lllll1l_opy_ (u"ࠣࡲࡵࡳࡽࡿࡓࡦࡶࡷ࡭ࡳ࡭ࡳࠣḕ")] = bstack1111l11lll1_opy_(bstack1111ll11l11_opy_, bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠤࡳࡶࡴࡾࡹࡔࡧࡷࡸ࡮ࡴࡧࡴࠤḖ")))
    bstack1111l1l1lll_opy_ = [element.lower() for element in bstack11l11llll11_opy_]
    bstack1111l1l111l_opy_(bstack111l11l1ll1_opy_, bstack1111l1l1lll_opy_)
    return bstack111l11l1ll1_opy_
def bstack1111l1l111l_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack1lllll1l_opy_ (u"ࠥ࠮࠯࠰ࠪࠣḗ")
    for value in d.values():
        if isinstance(value, dict):
            bstack1111l1l111l_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack1111l1l111l_opy_(item, keys)
def bstack1ll1l1ll11l_opy_():
    bstack1111l11ll1l_opy_ = [os.environ.get(bstack1lllll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡎࡒࡅࡔࡡࡇࡍࡗࠨḘ")), os.path.join(os.path.expanduser(bstack1lllll1l_opy_ (u"ࠧࢄࠢḙ")), bstack1lllll1l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭Ḛ")), os.path.join(bstack1lllll1l_opy_ (u"ࠧ࠰ࡶࡰࡴࠬḛ"), bstack1lllll1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨḜ"))]
    for path in bstack1111l11ll1l_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack1lllll1l_opy_ (u"ࠤࡉ࡭ࡱ࡫ࠠࠨࠤḝ") + str(path) + bstack1lllll1l_opy_ (u"ࠥࠫࠥ࡫ࡸࡪࡵࡷࡷ࠳ࠨḞ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack1lllll1l_opy_ (u"ࠦࡌ࡯ࡶࡪࡰࡪࠤࡵ࡫ࡲ࡮࡫ࡶࡷ࡮ࡵ࡮ࡴࠢࡩࡳࡷࠦࠧࠣḟ") + str(path) + bstack1lllll1l_opy_ (u"ࠧ࠭ࠢḠ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack1lllll1l_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࠬࠨḡ") + str(path) + bstack1lllll1l_opy_ (u"ࠢࠨࠢࡤࡰࡷ࡫ࡡࡥࡻࠣ࡬ࡦࡹࠠࡵࡪࡨࠤࡷ࡫ࡱࡶ࡫ࡵࡩࡩࠦࡰࡦࡴࡰ࡭ࡸࡹࡩࡰࡰࡶ࠲ࠧḢ"))
            else:
                logger.debug(bstack1lllll1l_opy_ (u"ࠣࡅࡵࡩࡦࡺࡩ࡯ࡩࠣࡪ࡮ࡲࡥࠡࠩࠥḣ") + str(path) + bstack1lllll1l_opy_ (u"ࠤࠪࠤࡼ࡯ࡴࡩࠢࡺࡶ࡮ࡺࡥࠡࡲࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲ࠳ࠨḤ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack1lllll1l_opy_ (u"ࠥࡓࡵ࡫ࡲࡢࡶ࡬ࡳࡳࠦࡳࡶࡥࡦࡩࡪࡪࡥࡥࠢࡩࡳࡷࠦࠧࠣḥ") + str(path) + bstack1lllll1l_opy_ (u"ࠦࠬ࠴ࠢḦ"))
            return path
        except Exception as e:
            logger.debug(bstack1lllll1l_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡻࡰࠡࡨ࡬ࡰࡪࠦࠧࡼࡲࡤࡸ࡭ࢃࠧ࠻ࠢࠥḧ") + str(e) + bstack1lllll1l_opy_ (u"ࠨࠢḨ"))
    logger.debug(bstack1lllll1l_opy_ (u"ࠢࡂ࡮࡯ࠤࡵࡧࡴࡩࡵࠣࡪࡦ࡯࡬ࡦࡦ࠱ࠦḩ"))
    return None
@measure(event_name=EVENTS.bstack11l11l1llll_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
def bstack1l11lll1ll1_opy_(binary_path, bstack1l1l1l11ll1_opy_, bs_config):
    logger.debug(bstack1lllll1l_opy_ (u"ࠣࡅࡸࡶࡷ࡫࡮ࡵࠢࡆࡐࡎࠦࡐࡢࡶ࡫ࠤ࡫ࡵࡵ࡯ࡦ࠽ࠤࢀࢃࠢḪ").format(binary_path))
    bstack111l11l1lll_opy_ = bstack1lllll1l_opy_ (u"ࠩࠪḫ")
    bstack111l1l111ll_opy_ = {
        bstack1lllll1l_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨḬ"): __version__,
        bstack1lllll1l_opy_ (u"ࠦࡴࡹࠢḭ"): platform.system(),
        bstack1lllll1l_opy_ (u"ࠧࡵࡳࡠࡣࡵࡧ࡭ࠨḮ"): platform.machine(),
        bstack1lllll1l_opy_ (u"ࠨࡣ࡭࡫ࡢࡺࡪࡸࡳࡪࡱࡱࠦḯ"): bstack1lllll1l_opy_ (u"ࠧ࠱ࠩḰ"),
        bstack1lllll1l_opy_ (u"ࠣࡵࡧ࡯ࡤࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠢḱ"): bstack1lllll1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩḲ")
    }
    bstack1111l1ll1l1_opy_(bstack111l1l111ll_opy_)
    try:
        if binary_path:
            bstack111l1l111ll_opy_[bstack1lllll1l_opy_ (u"ࠪࡧࡱ࡯࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨḳ")] = subprocess.check_output([binary_path, bstack1lllll1l_opy_ (u"ࠦࡻ࡫ࡲࡴ࡫ࡲࡲࠧḴ")]).strip().decode(bstack1lllll1l_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫḵ"))
        response = requests.request(
            bstack1lllll1l_opy_ (u"࠭ࡇࡆࡖࠪḶ"),
            url=bstack1l111ll1l1_opy_(bstack11l11ll11ll_opy_),
            headers=None,
            auth=(bs_config[bstack1lllll1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩḷ")], bs_config[bstack1lllll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫḸ")]),
            json=None,
            params=bstack111l1l111ll_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack1lllll1l_opy_ (u"ࠩࡸࡶࡱ࠭ḹ") in data.keys() and bstack1lllll1l_opy_ (u"ࠪࡹࡵࡪࡡࡵࡧࡧࡣࡨࡲࡩࡠࡸࡨࡶࡸ࡯࡯࡯ࠩḺ") in data.keys():
            logger.debug(bstack1lllll1l_opy_ (u"ࠦࡓ࡫ࡥࡥࠢࡷࡳࠥࡻࡰࡥࡣࡷࡩࠥࡨࡩ࡯ࡣࡵࡽ࠱ࠦࡣࡶࡴࡵࡩࡳࡺࠠࡣ࡫ࡱࡥࡷࡿࠠࡷࡧࡵࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠧḻ").format(bstack111l1l111ll_opy_[bstack1lllll1l_opy_ (u"ࠬࡩ࡬ࡪࡡࡹࡩࡷࡹࡩࡰࡰࠪḼ")]))
            if bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡉࡏࡃࡕ࡝ࡤ࡛ࡒࡍࠩḽ") in os.environ:
                logger.debug(bstack1lllll1l_opy_ (u"ࠢࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡥ࡭ࡳࡧࡲࡺࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡦࡹࠠࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡊࡐࡄࡖ࡞ࡥࡕࡓࡎࠣ࡭ࡸࠦࡳࡦࡶࠥḾ"))
                data[bstack1lllll1l_opy_ (u"ࠨࡷࡵࡰࠬḿ")] = os.environ[bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡗࡕࡐࠬṀ")]
            bstack1111l1l1l11_opy_ = bstack1111lllll11_opy_(data[bstack1lllll1l_opy_ (u"ࠪࡹࡷࡲࠧṁ")], bstack1l1l1l11ll1_opy_)
            bstack111l11l1lll_opy_ = os.path.join(bstack1l1l1l11ll1_opy_, bstack1111l1l1l11_opy_)
            os.chmod(bstack111l11l1lll_opy_, 0o777) # bstack111l11l1l1l_opy_ permission
            return bstack111l11l1lll_opy_
    except Exception as e:
        logger.debug(bstack1lllll1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠ࡯ࡧࡺࠤࡘࡊࡋࠡࡽࢀࠦṂ").format(e))
    return binary_path
def bstack1111l1ll1l1_opy_(bstack111l1l111ll_opy_):
    try:
        if bstack1lllll1l_opy_ (u"ࠬࡲࡩ࡯ࡷࡻࠫṃ") not in bstack111l1l111ll_opy_[bstack1lllll1l_opy_ (u"࠭࡯ࡴࠩṄ")].lower():
            return
        if os.path.exists(bstack1lllll1l_opy_ (u"ࠢ࠰ࡧࡷࡧ࠴ࡵࡳ࠮ࡴࡨࡰࡪࡧࡳࡦࠤṅ")):
            with open(bstack1lllll1l_opy_ (u"ࠣ࠱ࡨࡸࡨ࠵࡯ࡴ࠯ࡵࡩࡱ࡫ࡡࡴࡧࠥṆ"), bstack1lllll1l_opy_ (u"ࠤࡵࠦṇ")) as f:
                bstack1111ll1l1l1_opy_ = {}
                for line in f:
                    if bstack1lllll1l_opy_ (u"ࠥࡁࠧṈ") in line:
                        key, value = line.rstrip().split(bstack1lllll1l_opy_ (u"ࠦࡂࠨṉ"), 1)
                        bstack1111ll1l1l1_opy_[key] = value.strip(bstack1lllll1l_opy_ (u"ࠬࠨ࡜ࠨࠩṊ"))
                bstack111l1l111ll_opy_[bstack1lllll1l_opy_ (u"࠭ࡤࡪࡵࡷࡶࡴ࠭ṋ")] = bstack1111ll1l1l1_opy_.get(bstack1lllll1l_opy_ (u"ࠢࡊࡆࠥṌ"), bstack1lllll1l_opy_ (u"ࠣࠤṍ"))
        elif os.path.exists(bstack1lllll1l_opy_ (u"ࠤ࠲ࡩࡹࡩ࠯ࡢ࡮ࡳ࡭ࡳ࡫࠭ࡳࡧ࡯ࡩࡦࡹࡥࠣṎ")):
            bstack111l1l111ll_opy_[bstack1lllll1l_opy_ (u"ࠪࡨ࡮ࡹࡴࡳࡱࠪṏ")] = bstack1lllll1l_opy_ (u"ࠫࡦࡲࡰࡪࡰࡨࠫṐ")
    except Exception as e:
        logger.debug(bstack1lllll1l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡩࡨࡸࠥࡪࡩࡴࡶࡵࡳࠥࡵࡦࠡ࡮࡬ࡲࡺࡾࠢṑ") + e)
@measure(event_name=EVENTS.bstack11l11ll1l1l_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
def bstack1111lllll11_opy_(bstack1111l1ll11l_opy_, bstack1111l11l11l_opy_):
    logger.debug(bstack1lllll1l_opy_ (u"ࠨࡄࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡘࡊࡋࠡࡤ࡬ࡲࡦࡸࡹࠡࡨࡵࡳࡲࡀࠠࠣṒ") + str(bstack1111l1ll11l_opy_) + bstack1lllll1l_opy_ (u"ࠢࠣṓ"))
    zip_path = os.path.join(bstack1111l11l11l_opy_, bstack1lllll1l_opy_ (u"ࠣࡦࡲࡻࡳࡲ࡯ࡢࡦࡨࡨࡤ࡬ࡩ࡭ࡧ࠱ࡾ࡮ࡶࠢṔ"))
    bstack1111l1l1l11_opy_ = bstack1lllll1l_opy_ (u"ࠩࠪṕ")
    with requests.get(bstack1111l1ll11l_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack1lllll1l_opy_ (u"ࠥࡻࡧࠨṖ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack1lllll1l_opy_ (u"ࠦࡋ࡯࡬ࡦࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࡩࡩࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽ࠳ࠨṗ"))
    with zipfile.ZipFile(zip_path, bstack1lllll1l_opy_ (u"ࠬࡸࠧṘ")) as zip_ref:
        bstack1111lll1l11_opy_ = zip_ref.namelist()
        if len(bstack1111lll1l11_opy_) > 0:
            bstack1111l1l1l11_opy_ = bstack1111lll1l11_opy_[0] # bstack111l1l1l1ll_opy_ bstack11l11l1l1ll_opy_ will be bstack1111l11llll_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack1111l11l11l_opy_)
        logger.debug(bstack1lllll1l_opy_ (u"ࠨࡆࡪ࡮ࡨࡷࠥࡹࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࡮ࡼࠤࡪࡾࡴࡳࡣࡦࡸࡪࡪࠠࡵࡱࠣࠫࠧṙ") + str(bstack1111l11l11l_opy_) + bstack1lllll1l_opy_ (u"ࠢࠨࠤṚ"))
    os.remove(zip_path)
    return bstack1111l1l1l11_opy_
def get_cli_dir():
    bstack111l111111l_opy_ = bstack1ll1l1ll11l_opy_()
    if bstack111l111111l_opy_:
        bstack1l1l1l11ll1_opy_ = os.path.join(bstack111l111111l_opy_, bstack1lllll1l_opy_ (u"ࠣࡥ࡯࡭ࠧṛ"))
        if not os.path.exists(bstack1l1l1l11ll1_opy_):
            os.makedirs(bstack1l1l1l11ll1_opy_, mode=0o777, exist_ok=True)
        return bstack1l1l1l11ll1_opy_
    else:
        raise FileNotFoundError(bstack1lllll1l_opy_ (u"ࠤࡑࡳࠥࡽࡲࡪࡶࡤࡦࡱ࡫ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡔࡆࡎࠤࡧ࡯࡮ࡢࡴࡼ࠲ࠧṜ"))
def bstack1l1l1l1lll1_opy_(bstack1l1l1l11ll1_opy_):
    bstack1lllll1l_opy_ (u"ࠥࠦࠧࡍࡥࡵࠢࡷ࡬ࡪࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡘࡊࡋࠡࡤ࡬ࡲࡦࡸࡹࠡ࡫ࡱࠤࡦࠦࡷࡳ࡫ࡷࡥࡧࡲࡥࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼ࠲ࠧࠨࠢṝ")
    bstack111l1l11l11_opy_ = [
        os.path.join(bstack1l1l1l11ll1_opy_, f)
        for f in os.listdir(bstack1l1l1l11ll1_opy_)
        if os.path.isfile(os.path.join(bstack1l1l1l11ll1_opy_, f)) and f.startswith(bstack1lllll1l_opy_ (u"ࠦࡧ࡯࡮ࡢࡴࡼ࠱ࠧṞ"))
    ]
    if len(bstack111l1l11l11_opy_) > 0:
        return max(bstack111l1l11l11_opy_, key=os.path.getmtime) # get bstack1111llll1ll_opy_ binary
    return bstack1lllll1l_opy_ (u"ࠧࠨṟ")
def bstack111l11ll111_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l111l111ll_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l111l111ll_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack11l111l1ll_opy_(data, keys, default=None):
    bstack1lllll1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡓࡢࡨࡨࡰࡾࠦࡧࡦࡶࠣࡥࠥࡴࡥࡴࡶࡨࡨࠥࡼࡡ࡭ࡷࡨࠤ࡫ࡸ࡯࡮ࠢࡤࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹࠡࡱࡵࠤࡱ࡯ࡳࡵ࠰ࠍࠤࠥࠦࠠ࠻ࡲࡤࡶࡦࡳࠠࡥࡣࡷࡥ࠿ࠦࡔࡩࡧࠣࡨ࡮ࡩࡴࡪࡱࡱࡥࡷࡿࠠࡰࡴࠣࡰ࡮ࡹࡴࠡࡶࡲࠤࡹࡸࡡࡷࡧࡵࡷࡪ࠴ࠊࠡࠢࠣࠤ࠿ࡶࡡࡳࡣࡰࠤࡰ࡫ࡹࡴ࠼ࠣࡅࠥࡲࡩࡴࡶࠣࡳ࡫ࠦ࡫ࡦࡻࡶ࠳࡮ࡴࡤࡪࡥࡨࡷࠥࡸࡥࡱࡴࡨࡷࡪࡴࡴࡪࡰࡪࠤࡹ࡮ࡥࠡࡲࡤࡸ࡭࠴ࠊࠡࠢࠣࠤ࠿ࡶࡡࡳࡣࡰࠤࡩ࡫ࡦࡢࡷ࡯ࡸ࠿ࠦࡖࡢ࡮ࡸࡩࠥࡺ࡯ࠡࡴࡨࡸࡺࡸ࡮ࠡ࡫ࡩࠤࡹ࡮ࡥࠡࡲࡤࡸ࡭ࠦࡤࡰࡧࡶࠤࡳࡵࡴࠡࡧࡻ࡭ࡸࡺ࠮ࠋࠢࠣࠤࠥࡀࡲࡦࡶࡸࡶࡳࡀࠠࡕࡪࡨࠤࡻࡧ࡬ࡶࡧࠣࡥࡹࠦࡴࡩࡧࠣࡲࡪࡹࡴࡦࡦࠣࡴࡦࡺࡨ࠭ࠢࡲࡶࠥࡪࡥࡧࡣࡸࡰࡹࠦࡩࡧࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨ࠳ࠐࠠࠡࠢࠣࠦࠧࠨṠ")
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