# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
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
from bstack_utils.constants import (bstack1l11ll11l1_opy_, bstack1l1l1l111_opy_, bstack1lll1l1l1l_opy_,
                                    bstack11l1l11ll11_opy_, bstack11l1l11l1ll_opy_, bstack11l11ll1l1l_opy_, bstack11l1l1l11ll_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack111l111l1l_opy_, bstack111llllll_opy_
from bstack_utils.proxy import bstack1111l1ll1_opy_, bstack11l1l11l11_opy_
from bstack_utils.constants import *
from bstack_utils import bstack1l1l1l1111_opy_
from bstack_utils.bstack1l1l111ll1_opy_ import bstack111lll1ll_opy_
from browserstack_sdk._version import __version__
bstack1111ll11_opy_ = Config.bstack1llll11l1_opy_()
logger = bstack1l1l1l1111_opy_.get_logger(__name__, bstack1l1l1l1111_opy_.bstack1l1l1111l1l_opy_())
def bstack1111lll1ll1_opy_(config):
    return config[bstack1ll11_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᯊ")]
def bstack1111llll1l1_opy_(config):
    return config[bstack1ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᯋ")]
def bstack11l111ll1_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack111l11l1ll1_opy_(obj):
    values = []
    bstack111l1llll1l_opy_ = re.compile(bstack1ll11_opy_ (u"ࡶࠧࡤࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢࡠࡩ࠱ࠤࠣᯌ"), re.I)
    for key in obj.keys():
        if bstack111l1llll1l_opy_.match(key):
            values.append(obj[key])
    return values
def bstack111l1ll11ll_opy_(config):
    tags = []
    tags.extend(bstack111l11l1ll1_opy_(os.environ))
    tags.extend(bstack111l11l1ll1_opy_(config))
    return tags
def bstack1111ll11111_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111ll111111_opy_(bstack1111l1lll11_opy_):
    if not bstack1111l1lll11_opy_:
        return bstack1ll11_opy_ (u"ࠬ࠭ᯍ")
    return bstack1ll11_opy_ (u"ࠨࡻࡾࠢࠫࡿࢂ࠯ࠢᯎ").format(bstack1111l1lll11_opy_.name, bstack1111l1lll11_opy_.email)
def bstack1111ll111ll_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111l1l1l111_opy_ = repo.common_dir
        info = {
            bstack1ll11_opy_ (u"ࠢࡴࡪࡤࠦᯏ"): repo.head.commit.hexsha,
            bstack1ll11_opy_ (u"ࠣࡵ࡫ࡳࡷࡺ࡟ࡴࡪࡤࠦᯐ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack1ll11_opy_ (u"ࠤࡥࡶࡦࡴࡣࡩࠤᯑ"): repo.active_branch.name,
            bstack1ll11_opy_ (u"ࠥࡸࡦ࡭ࠢᯒ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack1ll11_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡸࡪࡸࠢᯓ"): bstack111ll111111_opy_(repo.head.commit.committer),
            bstack1ll11_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡹ࡫ࡲࡠࡦࡤࡸࡪࠨᯔ"): repo.head.commit.committed_datetime.isoformat(),
            bstack1ll11_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࠨᯕ"): bstack111ll111111_opy_(repo.head.commit.author),
            bstack1ll11_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸ࡟ࡥࡣࡷࡩࠧᯖ"): repo.head.commit.authored_datetime.isoformat(),
            bstack1ll11_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡠ࡯ࡨࡷࡸࡧࡧࡦࠤᯗ"): repo.head.commit.message,
            bstack1ll11_opy_ (u"ࠤࡵࡳࡴࡺࠢᯘ"): repo.git.rev_parse(bstack1ll11_opy_ (u"ࠥ࠱࠲ࡹࡨࡰࡹ࠰ࡸࡴࡶ࡬ࡦࡸࡨࡰࠧᯙ")),
            bstack1ll11_opy_ (u"ࠦࡨࡵ࡭࡮ࡱࡱࡣ࡬࡯ࡴࡠࡦ࡬ࡶࠧᯚ"): bstack111l1l1l111_opy_,
            bstack1ll11_opy_ (u"ࠧࡽ࡯ࡳ࡭ࡷࡶࡪ࡫࡟ࡨ࡫ࡷࡣࡩ࡯ࡲࠣᯛ"): subprocess.check_output([bstack1ll11_opy_ (u"ࠨࡧࡪࡶࠥᯜ"), bstack1ll11_opy_ (u"ࠢࡳࡧࡹ࠱ࡵࡧࡲࡴࡧࠥᯝ"), bstack1ll11_opy_ (u"ࠣ࠯࠰࡫࡮ࡺ࠭ࡤࡱࡰࡱࡴࡴ࠭ࡥ࡫ࡵࠦᯞ")]).strip().decode(
                bstack1ll11_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᯟ")),
            bstack1ll11_opy_ (u"ࠥࡰࡦࡹࡴࡠࡶࡤ࡫ࠧᯠ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack1ll11_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡷࡤࡹࡩ࡯ࡥࡨࡣࡱࡧࡳࡵࡡࡷࡥ࡬ࠨᯡ"): repo.git.rev_list(
                bstack1ll11_opy_ (u"ࠧࢁࡽ࠯࠰ࡾࢁࠧᯢ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1111ll1111l_opy_ = []
        for remote in remotes:
            bstack111l1llll11_opy_ = {
                bstack1ll11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᯣ"): remote.name,
                bstack1ll11_opy_ (u"ࠢࡶࡴ࡯ࠦᯤ"): remote.url,
            }
            bstack1111ll1111l_opy_.append(bstack111l1llll11_opy_)
        bstack111l11ll11l_opy_ = {
            bstack1ll11_opy_ (u"ࠣࡰࡤࡱࡪࠨᯥ"): bstack1ll11_opy_ (u"ࠤࡪ࡭ࡹࠨ᯦"),
            **info,
            bstack1ll11_opy_ (u"ࠥࡶࡪࡳ࡯ࡵࡧࡶࠦᯧ"): bstack1111ll1111l_opy_
        }
        bstack111l11ll11l_opy_ = bstack1111lll11l1_opy_(bstack111l11ll11l_opy_)
        return bstack111l11ll11l_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack1ll11_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡴࡶࡵ࡭ࡣࡷ࡭ࡳ࡭ࠠࡈ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢᯨ").format(err))
        return {}
def bstack11lll11l1l1_opy_(bstack111ll111ll1_opy_=None):
    bstack1ll11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡍࡥࡵࠢࡪ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡵࡳࡩࡨ࡯ࡦࡪࡥࡤࡰࡱࡿࠠࡧࡱࡵࡱࡦࡺࡴࡦࡦࠣࡪࡴࡸࠠࡂࡋࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦࡵࡴࡧࠣࡧࡦࡹࡥࡴࠢࡩࡳࡷࠦࡥࡢࡥ࡫ࠤ࡫ࡵ࡬ࡥࡧࡵࠤ࡮ࡴࠠࡵࡪࡨࠤࡱ࡯ࡳࡵ࠰ࠍࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡧࡱ࡯ࡨࡪࡸࡳࠡࠪ࡯࡭ࡸࡺࠬࠡࡱࡳࡸ࡮ࡵ࡮ࡢ࡮ࠬ࠾ࠥࡒࡩࡴࡶࠣࡳ࡫ࠦࡦࡰ࡮ࡧࡩࡷࠦࡰࡢࡶ࡫ࡷࠥࡺ࡯ࠡࡧࡻࡸࡷࡧࡣࡵࠢࡪ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡨࡵࡳࡲ࠴ࠠࡅࡧࡩࡥࡺࡲࡴࡴࠢࡷࡳࠥࡡ࡯ࡴ࠰ࡪࡩࡹࡩࡷࡥࠪࠬࡡ࠳ࠐࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࡬ࡪࡵࡷ࠾ࠥࡒࡩࡴࡶࠣࡳ࡫ࠦࡤࡪࡥࡷࡷ࠱ࠦࡥࡢࡥ࡫ࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮ࡴࡧࠡࡩ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡧࡱࡵࠤࡦࠦࡦࡰ࡮ࡧࡩࡷ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᯩ")
    if bstack111ll111ll1_opy_ == None: # bstack111l1l111l1_opy_ for bstack11lll111ll1_opy_-repo
        bstack111ll111ll1_opy_ = [os.getcwd()]
    results = []
    for folder in bstack111ll111ll1_opy_:
        try:
            repo = git.Repo(folder, search_parent_directories=True)
            result = {
                bstack1ll11_opy_ (u"ࠨࡰࡳࡋࡧࠦᯪ"): bstack1ll11_opy_ (u"ࠢࠣᯫ"),
                bstack1ll11_opy_ (u"ࠣࡨ࡬ࡰࡪࡹࡃࡩࡣࡱ࡫ࡪࡪࠢᯬ"): [],
                bstack1ll11_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡵࠥᯭ"): [],
                bstack1ll11_opy_ (u"ࠥࡴࡷࡊࡡࡵࡧࠥᯮ"): bstack1ll11_opy_ (u"ࠦࠧᯯ"),
                bstack1ll11_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡒ࡫ࡳࡴࡣࡪࡩࡸࠨᯰ"): [],
                bstack1ll11_opy_ (u"ࠨࡰࡳࡖ࡬ࡸࡱ࡫ࠢᯱ"): bstack1ll11_opy_ (u"᯲ࠢࠣ"),
                bstack1ll11_opy_ (u"ࠣࡲࡵࡈࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮᯳ࠣ"): bstack1ll11_opy_ (u"ࠤࠥ᯴"),
                bstack1ll11_opy_ (u"ࠥࡴࡷࡘࡡࡸࡆ࡬ࡪ࡫ࠨ᯵"): bstack1ll11_opy_ (u"ࠦࠧ᯶")
            }
            bstack111l1llllll_opy_ = repo.active_branch.name
            bstack111ll111l1l_opy_ = repo.head.commit
            result[bstack1ll11_opy_ (u"ࠧࡶࡲࡊࡦࠥ᯷")] = bstack111ll111l1l_opy_.hexsha
            bstack111l111l11l_opy_ = _111l11111ll_opy_(repo)
            logger.debug(bstack1ll11_opy_ (u"ࠨࡂࡢࡵࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤ࡫ࡵࡲࠡࡥࡲࡱࡵࡧࡲࡪࡵࡲࡲ࠿ࠦࠢ᯸") + str(bstack111l111l11l_opy_) + bstack1ll11_opy_ (u"ࠢࠣ᯹"))
            if bstack111l111l11l_opy_:
                try:
                    bstack111l1ll11l1_opy_ = repo.git.diff(bstack1ll11_opy_ (u"ࠣ࠯࠰ࡲࡦࡳࡥ࠮ࡱࡱࡰࡾࠨ᯺"), bstack1lll1llllll_opy_ (u"ࠤࡾࡦࡦࡹࡥࡠࡤࡵࡥࡳࡩࡨࡾ࠰࠱࠲ࢀࡩࡵࡳࡴࡨࡲࡹࡥࡢࡳࡣࡱࡧ࡭ࢃࠢ᯻")).split(bstack1ll11_opy_ (u"ࠪࡠࡳ࠭᯼"))
                    logger.debug(bstack1ll11_opy_ (u"ࠦࡈ࡮ࡡ࡯ࡩࡨࡨࠥ࡬ࡩ࡭ࡧࡶࠤࡧ࡫ࡴࡸࡧࡨࡲࠥࢁࡢࡢࡵࡨࡣࡧࡸࡡ࡯ࡥ࡫ࢁࠥࡧ࡮ࡥࠢࡾࡧࡺࡸࡲࡦࡰࡷࡣࡧࡸࡡ࡯ࡥ࡫ࢁ࠿ࠦࠢ᯽") + str(bstack111l1ll11l1_opy_) + bstack1ll11_opy_ (u"ࠧࠨ᯾"))
                    result[bstack1ll11_opy_ (u"ࠨࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠧ᯿")] = [f.strip() for f in bstack111l1ll11l1_opy_ if f.strip()]
                    commits = list(repo.iter_commits(bstack1lll1llllll_opy_ (u"ࠢࡼࡤࡤࡷࡪࡥࡢࡳࡣࡱࡧ࡭ࢃ࠮࠯ࡽࡦࡹࡷࡸࡥ࡯ࡶࡢࡦࡷࡧ࡮ࡤࡪࢀࠦᰀ")))
                except Exception:
                    logger.debug(bstack1ll11_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡬࡫ࡴࠡࡥ࡫ࡥࡳ࡭ࡥࡥࠢࡩ࡭ࡱ࡫ࡳࠡࡨࡵࡳࡲࠦࡢࡳࡣࡱࡧ࡭ࠦࡣࡰ࡯ࡳࡥࡷ࡯ࡳࡰࡰ࠱ࠤࡋࡧ࡬࡭࡫ࡱ࡫ࠥࡨࡡࡤ࡭ࠣࡸࡴࠦࡲࡦࡥࡨࡲࡹࠦࡣࡰ࡯ࡰ࡭ࡹࡹ࠮ࠣᰁ"))
                    commits = list(repo.iter_commits(max_count=10))
                    if commits:
                        result[bstack1ll11_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣᰂ")] = _1111lll11ll_opy_(commits[:5])
            else:
                commits = list(repo.iter_commits(max_count=10))
                if commits:
                    result[bstack1ll11_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤᰃ")] = _1111lll11ll_opy_(commits[:5])
            bstack111l1111111_opy_ = set()
            bstack1111llllll1_opy_ = []
            for commit in commits:
                logger.debug(bstack1ll11_opy_ (u"ࠦࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡥࡲࡱࡲ࡯ࡴ࠻ࠢࠥᰄ") + str(commit.message) + bstack1ll11_opy_ (u"ࠧࠨᰅ"))
                bstack111l1l11lll_opy_ = commit.author.name if commit.author else bstack1ll11_opy_ (u"ࠨࡕ࡯࡭ࡱࡳࡼࡴࠢᰆ")
                bstack111l1111111_opy_.add(bstack111l1l11lll_opy_)
                bstack1111llllll1_opy_.append({
                    bstack1ll11_opy_ (u"ࠢ࡮ࡧࡶࡷࡦ࡭ࡥࠣᰇ"): commit.message.strip(),
                    bstack1ll11_opy_ (u"ࠣࡷࡶࡩࡷࠨᰈ"): bstack111l1l11lll_opy_
                })
            result[bstack1ll11_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࡵࠥᰉ")] = list(bstack111l1111111_opy_)
            result[bstack1ll11_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡐࡩࡸࡹࡡࡨࡧࡶࠦᰊ")] = bstack1111llllll1_opy_
            result[bstack1ll11_opy_ (u"ࠦࡵࡸࡄࡢࡶࡨࠦᰋ")] = bstack111ll111l1l_opy_.committed_datetime.strftime(bstack1ll11_opy_ (u"࡙ࠧࠫ࠮ࠧࡰ࠱ࠪࡪࠢᰌ"))
            if (not result[bstack1ll11_opy_ (u"ࠨࡰࡳࡖ࡬ࡸࡱ࡫ࠢᰍ")] or result[bstack1ll11_opy_ (u"ࠢࡱࡴࡗ࡭ࡹࡲࡥࠣᰎ")].strip() == bstack1ll11_opy_ (u"ࠣࠤᰏ")) and bstack111ll111l1l_opy_.message:
                bstack111l111111l_opy_ = bstack111ll111l1l_opy_.message.strip().splitlines()
                result[bstack1ll11_opy_ (u"ࠤࡳࡶ࡙࡯ࡴ࡭ࡧࠥᰐ")] = bstack111l111111l_opy_[0] if bstack111l111111l_opy_ else bstack1ll11_opy_ (u"ࠥࠦᰑ")
                if len(bstack111l111111l_opy_) > 2:
                    result[bstack1ll11_opy_ (u"ࠦࡵࡸࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠦᰒ")] = bstack1ll11_opy_ (u"ࠬࡢ࡮ࠨᰓ").join(bstack111l111111l_opy_[2:]).strip()
            results.append(result)
        except Exception as err:
            logger.error(bstack1ll11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡯ࡱࡷ࡯ࡥࡹ࡯࡮ࡨࠢࡊ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡨࡲࡶࠥࡇࡉࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱࠤ࠭࡬࡯࡭ࡦࡨࡶ࠿ࠦࡻࡧࡱ࡯ࡨࡪࡸࡽࠪ࠼ࠣࠦᰔ") + str(err) + bstack1ll11_opy_ (u"ࠢࠣᰕ"))
    filtered_results = [
        result
        for result in results
        if _111l1ll1ll1_opy_(result)
    ]
    return filtered_results
def _111l1ll1ll1_opy_(result):
    bstack1ll11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡊࡨࡰࡵ࡫ࡲࠡࡶࡲࠤࡨ࡮ࡥࡤ࡭ࠣ࡭࡫ࠦࡡࠡࡩ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡳࡧࡶࡹࡱࡺࠠࡪࡵࠣࡺࡦࡲࡩࡥࠢࠫࡲࡴࡴ࠭ࡦ࡯ࡳࡸࡾࠦࡦࡪ࡮ࡨࡷࡈ࡮ࡡ࡯ࡩࡨࡨࠥࡧ࡮ࡥࠢࡤࡹࡹ࡮࡯ࡳࡵࠬ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᰖ")
    return (
        isinstance(result.get(bstack1ll11_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡳࡄࡪࡤࡲ࡬࡫ࡤࠣᰗ"), None), list)
        and len(result[bstack1ll11_opy_ (u"ࠥࡪ࡮ࡲࡥࡴࡅ࡫ࡥࡳ࡭ࡥࡥࠤᰘ")]) > 0
        and isinstance(result.get(bstack1ll11_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡷࠧᰙ"), None), list)
        and len(result[bstack1ll11_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡸࠨᰚ")]) > 0
    )
def _111l11111ll_opy_(repo):
    bstack1ll11_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡔࡳࡻࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡷ࡬ࡪࠦࡢࡢࡵࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥ࡭ࡩࡷࡧࡱࠤࡷ࡫ࡰࡰࠢࡺ࡭ࡹ࡮࡯ࡶࡶࠣ࡬ࡦࡸࡤࡤࡱࡧࡩࡩࠦ࡮ࡢ࡯ࡨࡷࠥࡧ࡮ࡥࠢࡺࡳࡷࡱࠠࡸ࡫ࡷ࡬ࠥࡧ࡬࡭࡙ࠢࡇࡘࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡲࡴ࠰ࠍࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡪࡥࡧࡣࡸࡰࡹࠦࡢࡳࡣࡱࡧ࡭ࠦࡩࡧࠢࡳࡳࡸࡹࡩࡣ࡮ࡨ࠰ࠥ࡫࡬ࡴࡧࠣࡒࡴࡴࡥ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᰛ")
    try:
        try:
            origin = repo.remotes.origin
            bstack111l1ll1l11_opy_ = origin.refs[bstack1ll11_opy_ (u"ࠧࡉࡇࡄࡈࠬᰜ")]
            target = bstack111l1ll1l11_opy_.reference.name
            if target.startswith(bstack1ll11_opy_ (u"ࠨࡱࡵ࡭࡬࡯࡮࠰ࠩᰝ")):
                return target
        except Exception:
            pass
        if repo.remotes and repo.remotes.origin.refs:
            for ref in repo.remotes.origin.refs:
                if ref.name.startswith(bstack1ll11_opy_ (u"ࠩࡲࡶ࡮࡭ࡩ࡯࠱ࠪᰞ")):
                    return ref.name
        if repo.heads:
            return repo.heads[0].name
    except Exception:
        pass
    return None
def _1111lll11ll_opy_(commits):
    bstack1ll11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡋࡪࡺࠠ࡭࡫ࡶࡸࠥࡵࡦࠡࡥ࡫ࡥࡳ࡭ࡥࡥࠢࡩ࡭ࡱ࡫ࡳࠡࡨࡵࡳࡲࠦࡡࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢࡦࡳࡲࡳࡩࡵࡵ࠱ࠎࠥࠦࠠࠡࠤࠥࠦᰟ")
    bstack111l1ll11l1_opy_ = set()
    try:
        for commit in commits:
            if commit.parents:
                for parent in commit.parents:
                    diff = commit.diff(parent)
                    for bstack111l1l1l1l1_opy_ in diff:
                        if bstack111l1l1l1l1_opy_.a_path:
                            bstack111l1ll11l1_opy_.add(bstack111l1l1l1l1_opy_.a_path)
                        if bstack111l1l1l1l1_opy_.b_path:
                            bstack111l1ll11l1_opy_.add(bstack111l1l1l1l1_opy_.b_path)
    except Exception:
        pass
    return list(bstack111l1ll11l1_opy_)
def bstack1111lll11l1_opy_(bstack111l11ll11l_opy_):
    bstack1111l1llll1_opy_ = bstack111ll111l11_opy_(bstack111l11ll11l_opy_)
    if bstack1111l1llll1_opy_ and bstack1111l1llll1_opy_ > bstack11l1l11ll11_opy_:
        bstack1111ll1ll1l_opy_ = bstack1111l1llll1_opy_ - bstack11l1l11ll11_opy_
        bstack1111lll1111_opy_ = bstack1111lllllll_opy_(bstack111l11ll11l_opy_[bstack1ll11_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧᰠ")], bstack1111ll1ll1l_opy_)
        bstack111l11ll11l_opy_[bstack1ll11_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡤࡳࡥࡴࡵࡤ࡫ࡪࠨᰡ")] = bstack1111lll1111_opy_
        logger.info(bstack1ll11_opy_ (u"ࠨࡔࡩࡧࠣࡧࡴࡳ࡭ࡪࡶࠣ࡬ࡦࡹࠠࡣࡧࡨࡲࠥࡺࡲࡶࡰࡦࡥࡹ࡫ࡤ࠯ࠢࡖ࡭ࡿ࡫ࠠࡰࡨࠣࡧࡴࡳ࡭ࡪࡶࠣࡥ࡫ࡺࡥࡳࠢࡷࡶࡺࡴࡣࡢࡶ࡬ࡳࡳࠦࡩࡴࠢࡾࢁࠥࡑࡂࠣᰢ")
                    .format(bstack111ll111l11_opy_(bstack111l11ll11l_opy_) / 1024))
    return bstack111l11ll11l_opy_
def bstack111ll111l11_opy_(json_data):
    try:
        if json_data:
            bstack111l11l1lll_opy_ = json.dumps(json_data)
            bstack111l1111l11_opy_ = sys.getsizeof(bstack111l11l1lll_opy_)
            return bstack111l1111l11_opy_
    except Exception as e:
        logger.debug(bstack1ll11_opy_ (u"ࠢࡔࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭ࠠࡸࡪ࡬ࡰࡪࠦࡣࡢ࡮ࡦࡹࡱࡧࡴࡪࡰࡪࠤࡸ࡯ࡺࡦࠢࡲࡪࠥࡐࡓࡐࡐࠣࡳࡧࡰࡥࡤࡶ࠽ࠤࢀࢃࠢᰣ").format(e))
    return -1
def bstack1111lllllll_opy_(field, bstack111l1l1l11l_opy_):
    try:
        bstack111l111l1l1_opy_ = len(bytes(bstack11l1l11l1ll_opy_, bstack1ll11_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᰤ")))
        bstack111l111ll11_opy_ = bytes(field, bstack1ll11_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᰥ"))
        bstack111l1ll111l_opy_ = len(bstack111l111ll11_opy_)
        bstack1111llll111_opy_ = ceil(bstack111l1ll111l_opy_ - bstack111l1l1l11l_opy_ - bstack111l111l1l1_opy_)
        if bstack1111llll111_opy_ > 0:
            bstack111l1111l1l_opy_ = bstack111l111ll11_opy_[:bstack1111llll111_opy_].decode(bstack1ll11_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᰦ"), errors=bstack1ll11_opy_ (u"ࠫ࡮࡭࡮ࡰࡴࡨࠫᰧ")) + bstack11l1l11l1ll_opy_
            return bstack111l1111l1l_opy_
    except Exception as e:
        logger.debug(bstack1ll11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡸࡷࡻ࡮ࡤࡣࡷ࡭ࡳ࡭ࠠࡧ࡫ࡨࡰࡩ࠲ࠠ࡯ࡱࡷ࡬࡮ࡴࡧࠡࡹࡤࡷࠥࡺࡲࡶࡰࡦࡥࡹ࡫ࡤࠡࡪࡨࡶࡪࡀࠠࡼࡿࠥᰨ").format(e))
    return field
def bstack1l11l1l11l_opy_():
    env = os.environ
    if (bstack1ll11_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡖࡔࡏࠦᰩ") in env and len(env[bstack1ll11_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡗࡕࡐࠧᰪ")]) > 0) or (
            bstack1ll11_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡋࡓࡒࡋࠢᰫ") in env and len(env[bstack1ll11_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢࡌࡔࡓࡅࠣᰬ")]) > 0):
        return {
            bstack1ll11_opy_ (u"ࠥࡲࡦࡳࡥࠣᰭ"): bstack1ll11_opy_ (u"ࠦࡏ࡫࡮࡬࡫ࡱࡷࠧᰮ"),
            bstack1ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᰯ"): env.get(bstack1ll11_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᰰ")),
            bstack1ll11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᰱ"): env.get(bstack1ll11_opy_ (u"ࠣࡌࡒࡆࡤࡔࡁࡎࡇࠥᰲ")),
            bstack1ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᰳ"): env.get(bstack1ll11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᰴ"))
        }
    if env.get(bstack1ll11_opy_ (u"ࠦࡈࡏࠢᰵ")) == bstack1ll11_opy_ (u"ࠧࡺࡲࡶࡧࠥᰶ") and bstack1llll1lll1_opy_(env.get(bstack1ll11_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡉࡉ᰷ࠣ"))):
        return {
            bstack1ll11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᰸"): bstack1ll11_opy_ (u"ࠣࡅ࡬ࡶࡨࡲࡥࡄࡋࠥ᰹"),
            bstack1ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᰺"): env.get(bstack1ll11_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨ᰻")),
            bstack1ll11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᰼"): env.get(bstack1ll11_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡐࡏࡃࠤ᰽")),
            bstack1ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᰾"): env.get(bstack1ll11_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࠥ᰿"))
        }
    if env.get(bstack1ll11_opy_ (u"ࠣࡅࡌࠦ᱀")) == bstack1ll11_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ᱁") and bstack1llll1lll1_opy_(env.get(bstack1ll11_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࠥ᱂"))):
        return {
            bstack1ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᱃"): bstack1ll11_opy_ (u"࡚ࠧࡲࡢࡸ࡬ࡷࠥࡉࡉࠣ᱄"),
            bstack1ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᱅"): env.get(bstack1ll11_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡃࡗࡌࡐࡉࡥࡗࡆࡄࡢ࡙ࡗࡒࠢ᱆")),
            bstack1ll11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᱇"): env.get(bstack1ll11_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦ᱈")),
            bstack1ll11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᱉"): env.get(bstack1ll11_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥ᱊"))
        }
    if env.get(bstack1ll11_opy_ (u"ࠧࡉࡉࠣ᱋")) == bstack1ll11_opy_ (u"ࠨࡴࡳࡷࡨࠦ᱌") and env.get(bstack1ll11_opy_ (u"ࠢࡄࡋࡢࡒࡆࡓࡅࠣᱍ")) == bstack1ll11_opy_ (u"ࠣࡥࡲࡨࡪࡹࡨࡪࡲࠥᱎ"):
        return {
            bstack1ll11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᱏ"): bstack1ll11_opy_ (u"ࠥࡇࡴࡪࡥࡴࡪ࡬ࡴࠧ᱐"),
            bstack1ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᱑"): None,
            bstack1ll11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᱒"): None,
            bstack1ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᱓"): None
        }
    if env.get(bstack1ll11_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡆࡗࡇࡎࡄࡊࠥ᱔")) and env.get(bstack1ll11_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡈࡕࡍࡎࡋࡗࠦ᱕")):
        return {
            bstack1ll11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ᱖"): bstack1ll11_opy_ (u"ࠥࡆ࡮ࡺࡢࡶࡥ࡮ࡩࡹࠨ᱗"),
            bstack1ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢ᱘"): env.get(bstack1ll11_opy_ (u"ࠧࡈࡉࡕࡄࡘࡇࡐࡋࡔࡠࡉࡌࡘࡤࡎࡔࡕࡒࡢࡓࡗࡏࡇࡊࡐࠥ᱙")),
            bstack1ll11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᱚ"): None,
            bstack1ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᱛ"): env.get(bstack1ll11_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᱜ"))
        }
    if env.get(bstack1ll11_opy_ (u"ࠤࡆࡍࠧᱝ")) == bstack1ll11_opy_ (u"ࠥࡸࡷࡻࡥࠣᱞ") and bstack1llll1lll1_opy_(env.get(bstack1ll11_opy_ (u"ࠦࡉࡘࡏࡏࡇࠥᱟ"))):
        return {
            bstack1ll11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᱠ"): bstack1ll11_opy_ (u"ࠨࡄࡳࡱࡱࡩࠧᱡ"),
            bstack1ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᱢ"): env.get(bstack1ll11_opy_ (u"ࠣࡆࡕࡓࡓࡋ࡟ࡃࡗࡌࡐࡉࡥࡌࡊࡐࡎࠦᱣ")),
            bstack1ll11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᱤ"): None,
            bstack1ll11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᱥ"): env.get(bstack1ll11_opy_ (u"ࠦࡉࡘࡏࡏࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᱦ"))
        }
    if env.get(bstack1ll11_opy_ (u"ࠧࡉࡉࠣᱧ")) == bstack1ll11_opy_ (u"ࠨࡴࡳࡷࡨࠦᱨ") and bstack1llll1lll1_opy_(env.get(bstack1ll11_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࠥᱩ"))):
        return {
            bstack1ll11_opy_ (u"ࠣࡰࡤࡱࡪࠨᱪ"): bstack1ll11_opy_ (u"ࠤࡖࡩࡲࡧࡰࡩࡱࡵࡩࠧᱫ"),
            bstack1ll11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᱬ"): env.get(bstack1ll11_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡐࡔࡊࡅࡓࡏ࡚ࡂࡖࡌࡓࡓࡥࡕࡓࡎࠥᱭ")),
            bstack1ll11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᱮ"): env.get(bstack1ll11_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᱯ")),
            bstack1ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᱰ"): env.get(bstack1ll11_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡋࡇࠦᱱ"))
        }
    if env.get(bstack1ll11_opy_ (u"ࠤࡆࡍࠧᱲ")) == bstack1ll11_opy_ (u"ࠥࡸࡷࡻࡥࠣᱳ") and bstack1llll1lll1_opy_(env.get(bstack1ll11_opy_ (u"ࠦࡌࡏࡔࡍࡃࡅࡣࡈࡏࠢᱴ"))):
        return {
            bstack1ll11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᱵ"): bstack1ll11_opy_ (u"ࠨࡇࡪࡶࡏࡥࡧࠨᱶ"),
            bstack1ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᱷ"): env.get(bstack1ll11_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡗࡕࡐࠧᱸ")),
            bstack1ll11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᱹ"): env.get(bstack1ll11_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᱺ")),
            bstack1ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᱻ"): env.get(bstack1ll11_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡏࡄࠣᱼ"))
        }
    if env.get(bstack1ll11_opy_ (u"ࠨࡃࡊࠤᱽ")) == bstack1ll11_opy_ (u"ࠢࡵࡴࡸࡩࠧ᱾") and bstack1llll1lll1_opy_(env.get(bstack1ll11_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࠦ᱿"))):
        return {
            bstack1ll11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᲀ"): bstack1ll11_opy_ (u"ࠥࡆࡺ࡯࡬ࡥ࡭࡬ࡸࡪࠨᲁ"),
            bstack1ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᲂ"): env.get(bstack1ll11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᲃ")),
            bstack1ll11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᲄ"): env.get(bstack1ll11_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡐࡆࡈࡅࡍࠤᲅ")) or env.get(bstack1ll11_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡎࡂࡏࡈࠦᲆ")),
            bstack1ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᲇ"): env.get(bstack1ll11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᲈ"))
        }
    if bstack1llll1lll1_opy_(env.get(bstack1ll11_opy_ (u"࡙ࠦࡌ࡟ࡃࡗࡌࡐࡉࠨᲉ"))):
        return {
            bstack1ll11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᲊ"): bstack1ll11_opy_ (u"ࠨࡖࡪࡵࡸࡥࡱࠦࡓࡵࡷࡧ࡭ࡴࠦࡔࡦࡣࡰࠤࡘ࡫ࡲࡷ࡫ࡦࡩࡸࠨ᲋"),
            bstack1ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᲌"): bstack1ll11_opy_ (u"ࠣࡽࢀࡿࢂࠨ᲍").format(env.get(bstack1ll11_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡆࡐࡗࡑࡈࡆ࡚ࡉࡐࡐࡖࡉࡗ࡜ࡅࡓࡗࡕࡍࠬ᲎")), env.get(bstack1ll11_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡑࡔࡒࡎࡊࡉࡔࡊࡆࠪ᲏"))),
            bstack1ll11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᲐ"): env.get(bstack1ll11_opy_ (u"࡙࡙ࠧࡔࡖࡈࡑࡤࡊࡅࡇࡋࡑࡍ࡙ࡏࡏࡏࡋࡇࠦᲑ")),
            bstack1ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᲒ"): env.get(bstack1ll11_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢᲓ"))
        }
    if bstack1llll1lll1_opy_(env.get(bstack1ll11_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࠥᲔ"))):
        return {
            bstack1ll11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᲕ"): bstack1ll11_opy_ (u"ࠥࡅࡵࡶࡶࡦࡻࡲࡶࠧᲖ"),
            bstack1ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᲗ"): bstack1ll11_opy_ (u"ࠧࢁࡽ࠰ࡲࡵࡳ࡯࡫ࡣࡵ࠱ࡾࢁ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠦᲘ").format(env.get(bstack1ll11_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡗࡕࡐࠬᲙ")), env.get(bstack1ll11_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡄࡇࡈࡕࡕࡏࡖࡢࡒࡆࡓࡅࠨᲚ")), env.get(bstack1ll11_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡔࡗࡕࡊࡆࡅࡗࡣࡘࡒࡕࡈࠩᲛ")), env.get(bstack1ll11_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭Ნ"))),
            bstack1ll11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᲝ"): env.get(bstack1ll11_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣᲞ")),
            bstack1ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᲟ"): env.get(bstack1ll11_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᲠ"))
        }
    if env.get(bstack1ll11_opy_ (u"ࠢࡂ࡜ࡘࡖࡊࡥࡈࡕࡖࡓࡣ࡚࡙ࡅࡓࡡࡄࡋࡊࡔࡔࠣᲡ")) and env.get(bstack1ll11_opy_ (u"ࠣࡖࡉࡣࡇ࡛ࡉࡍࡆࠥᲢ")):
        return {
            bstack1ll11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᲣ"): bstack1ll11_opy_ (u"ࠥࡅࡿࡻࡲࡦࠢࡆࡍࠧᲤ"),
            bstack1ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᲥ"): bstack1ll11_opy_ (u"ࠧࢁࡽࡼࡿ࠲ࡣࡧࡻࡩ࡭ࡦ࠲ࡶࡪࡹࡵ࡭ࡶࡶࡃࡧࡻࡩ࡭ࡦࡌࡨࡂࢁࡽࠣᲦ").format(env.get(bstack1ll11_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡊࡔ࡛ࡎࡅࡃࡗࡍࡔࡔࡓࡆࡔ࡙ࡉࡗ࡛ࡒࡊࠩᲧ")), env.get(bstack1ll11_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡕࡘࡏࡋࡇࡆࡘࠬᲨ")), env.get(bstack1ll11_opy_ (u"ࠨࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠨᲩ"))),
            bstack1ll11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᲪ"): env.get(bstack1ll11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠥᲫ")),
            bstack1ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᲬ"): env.get(bstack1ll11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧᲭ"))
        }
    if any([env.get(bstack1ll11_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᲮ")), env.get(bstack1ll11_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡖࡊ࡙ࡏࡍࡘࡈࡈࡤ࡙ࡏࡖࡔࡆࡉࡤ࡜ࡅࡓࡕࡌࡓࡓࠨᲯ")), env.get(bstack1ll11_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡘࡕࡕࡓࡅࡈࡣ࡛ࡋࡒࡔࡋࡒࡒࠧᲰ"))]):
        return {
            bstack1ll11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᲱ"): bstack1ll11_opy_ (u"ࠥࡅ࡜࡙ࠠࡄࡱࡧࡩࡇࡻࡩ࡭ࡦࠥᲲ"),
            bstack1ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᲳ"): env.get(bstack1ll11_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡒࡘࡆࡑࡏࡃࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᲴ")),
            bstack1ll11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᲵ"): env.get(bstack1ll11_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᲶ")),
            bstack1ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᲷ"): env.get(bstack1ll11_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢᲸ"))
        }
    if env.get(bstack1ll11_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡐࡸࡱࡧ࡫ࡲࠣᲹ")):
        return {
            bstack1ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᲺ"): bstack1ll11_opy_ (u"ࠧࡈࡡ࡮ࡤࡲࡳࠧ᲻"),
            bstack1ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᲼"): env.get(bstack1ll11_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡘࡥࡴࡷ࡯ࡸࡸ࡛ࡲ࡭ࠤᲽ")),
            bstack1ll11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᲾ"): env.get(bstack1ll11_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡶ࡬ࡴࡸࡴࡋࡱࡥࡒࡦࡳࡥࠣᲿ")),
            bstack1ll11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳀"): env.get(bstack1ll11_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡧࡻࡩ࡭ࡦࡑࡹࡲࡨࡥࡳࠤ᳁"))
        }
    if env.get(bstack1ll11_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࠨ᳂")) or env.get(bstack1ll11_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡎࡃࡌࡒࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡔࡖࡄࡖ࡙ࡋࡄࠣ᳃")):
        return {
            bstack1ll11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᳄"): bstack1ll11_opy_ (u"࡙ࠣࡨࡶࡨࡱࡥࡳࠤ᳅"),
            bstack1ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᳆"): env.get(bstack1ll11_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢ᳇")),
            bstack1ll11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᳈"): bstack1ll11_opy_ (u"ࠧࡓࡡࡪࡰࠣࡔ࡮ࡶࡥ࡭࡫ࡱࡩࠧ᳉") if env.get(bstack1ll11_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡎࡃࡌࡒࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡔࡖࡄࡖ࡙ࡋࡄࠣ᳊")) else None,
            bstack1ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᳋"): env.get(bstack1ll11_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡊࡍ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨ᳌"))
        }
    if any([env.get(bstack1ll11_opy_ (u"ࠤࡊࡇࡕࡥࡐࡓࡑࡍࡉࡈ࡚ࠢ᳍")), env.get(bstack1ll11_opy_ (u"ࠥࡋࡈࡒࡏࡖࡆࡢࡔࡗࡕࡊࡆࡅࡗࠦ᳎")), env.get(bstack1ll11_opy_ (u"ࠦࡌࡕࡏࡈࡎࡈࡣࡈࡒࡏࡖࡆࡢࡔࡗࡕࡊࡆࡅࡗࠦ᳏"))]):
        return {
            bstack1ll11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ᳐"): bstack1ll11_opy_ (u"ࠨࡇࡰࡱࡪࡰࡪࠦࡃ࡭ࡱࡸࡨࠧ᳑"),
            bstack1ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ᳒"): None,
            bstack1ll11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᳓"): env.get(bstack1ll11_opy_ (u"ࠤࡓࡖࡔࡐࡅࡄࡖࡢࡍࡉࠨ᳔")),
            bstack1ll11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᳕"): env.get(bstack1ll11_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨ᳖"))
        }
    if env.get(bstack1ll11_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅ᳗ࠣ")):
        return {
            bstack1ll11_opy_ (u"ࠨ࡮ࡢ࡯ࡨ᳘ࠦ"): bstack1ll11_opy_ (u"ࠢࡔࡪ࡬ࡴࡵࡧࡢ࡭ࡧ᳙ࠥ"),
            bstack1ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᳚"): env.get(bstack1ll11_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣ᳛")),
            bstack1ll11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩ᳜ࠧ"): bstack1ll11_opy_ (u"ࠦࡏࡵࡢࠡࠥࡾࢁ᳝ࠧ").format(env.get(bstack1ll11_opy_ (u"࡙ࠬࡈࡊࡒࡓࡅࡇࡒࡅࡠࡌࡒࡆࡤࡏࡄࠨ᳞"))) if env.get(bstack1ll11_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡍࡓࡇࡥࡉࡅࠤ᳟")) else None,
            bstack1ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ᳠"): env.get(bstack1ll11_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥ᳡"))
        }
    if bstack1llll1lll1_opy_(env.get(bstack1ll11_opy_ (u"ࠤࡑࡉ࡙ࡒࡉࡇ᳢࡛ࠥ"))):
        return {
            bstack1ll11_opy_ (u"ࠥࡲࡦࡳࡥ᳣ࠣ"): bstack1ll11_opy_ (u"ࠦࡓ࡫ࡴ࡭࡫ࡩࡽ᳤ࠧ"),
            bstack1ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬᳥ࠣ"): env.get(bstack1ll11_opy_ (u"ࠨࡄࡆࡒࡏࡓ࡞ࡥࡕࡓࡎ᳦ࠥ")),
            bstack1ll11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ᳧"): env.get(bstack1ll11_opy_ (u"ࠣࡕࡌࡘࡊࡥࡎࡂࡏࡈ᳨ࠦ")),
            bstack1ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᳩ"): env.get(bstack1ll11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᳪ"))
        }
    if bstack1llll1lll1_opy_(env.get(bstack1ll11_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣࡆࡉࡔࡊࡑࡑࡗࠧᳫ"))):
        return {
            bstack1ll11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᳬ"): bstack1ll11_opy_ (u"ࠨࡇࡪࡶࡋࡹࡧࠦࡁࡤࡶ࡬ࡳࡳࡹ᳭ࠢ"),
            bstack1ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᳮ"): bstack1ll11_opy_ (u"ࠣࡽࢀ࠳ࢀࢃ࠯ࡢࡥࡷ࡭ࡴࡴࡳ࠰ࡴࡸࡲࡸ࠵ࡻࡾࠤᳯ").format(env.get(bstack1ll11_opy_ (u"ࠩࡊࡍ࡙ࡎࡕࡃࡡࡖࡉࡗ࡜ࡅࡓࡡࡘࡖࡑ࠭ᳰ")), env.get(bstack1ll11_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡖࡊࡖࡏࡔࡋࡗࡓࡗ࡟ࠧᳱ")), env.get(bstack1ll11_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡗ࡛ࡎࡠࡋࡇࠫᳲ"))),
            bstack1ll11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᳳ"): env.get(bstack1ll11_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡗࡐࡔࡎࡊࡑࡕࡗࠣ᳴")),
            bstack1ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᳵ"): env.get(bstack1ll11_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠࡔࡘࡒࡤࡏࡄࠣᳶ"))
        }
    if env.get(bstack1ll11_opy_ (u"ࠤࡆࡍࠧ᳷")) == bstack1ll11_opy_ (u"ࠥࡸࡷࡻࡥࠣ᳸") and env.get(bstack1ll11_opy_ (u"࡛ࠦࡋࡒࡄࡇࡏࠦ᳹")) == bstack1ll11_opy_ (u"ࠧ࠷ࠢᳺ"):
        return {
            bstack1ll11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ᳻"): bstack1ll11_opy_ (u"ࠢࡗࡧࡵࡧࡪࡲࠢ᳼"),
            bstack1ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦ᳽"): bstack1ll11_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࡾࢁࠧ᳾").format(env.get(bstack1ll11_opy_ (u"࡚ࠪࡊࡘࡃࡆࡎࡢ࡙ࡗࡒࠧ᳿"))),
            bstack1ll11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᴀ"): None,
            bstack1ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴁ"): None,
        }
    if env.get(bstack1ll11_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡘࡈࡖࡘࡏࡏࡏࠤᴂ")):
        return {
            bstack1ll11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᴃ"): bstack1ll11_opy_ (u"ࠣࡖࡨࡥࡲࡩࡩࡵࡻࠥᴄ"),
            bstack1ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᴅ"): None,
            bstack1ll11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴆ"): env.get(bstack1ll11_opy_ (u"࡙ࠦࡋࡁࡎࡅࡌࡘ࡞ࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡏࡃࡐࡉࠧᴇ")),
            bstack1ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴈ"): env.get(bstack1ll11_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᴉ"))
        }
    if any([env.get(bstack1ll11_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࠥᴊ")), env.get(bstack1ll11_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࡣ࡚ࡘࡌࠣᴋ")), env.get(bstack1ll11_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠢᴌ")), env.get(bstack1ll11_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡔࡆࡃࡐࠦᴍ"))]):
        return {
            bstack1ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᴎ"): bstack1ll11_opy_ (u"ࠧࡉ࡯࡯ࡥࡲࡹࡷࡹࡥࠣᴏ"),
            bstack1ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᴐ"): None,
            bstack1ll11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᴑ"): env.get(bstack1ll11_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᴒ")) or None,
            bstack1ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᴓ"): env.get(bstack1ll11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᴔ"), 0)
        }
    if env.get(bstack1ll11_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤᴕ")):
        return {
            bstack1ll11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᴖ"): bstack1ll11_opy_ (u"ࠨࡇࡰࡅࡇࠦᴗ"),
            bstack1ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᴘ"): None,
            bstack1ll11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᴙ"): env.get(bstack1ll11_opy_ (u"ࠤࡊࡓࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᴚ")),
            bstack1ll11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᴛ"): env.get(bstack1ll11_opy_ (u"ࠦࡌࡕ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡆࡓ࡚ࡔࡔࡆࡔࠥᴜ"))
        }
    if env.get(bstack1ll11_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᴝ")):
        return {
            bstack1ll11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᴞ"): bstack1ll11_opy_ (u"ࠢࡄࡱࡧࡩࡋࡸࡥࡴࡪࠥᴟ"),
            bstack1ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᴠ"): env.get(bstack1ll11_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᴡ")),
            bstack1ll11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᴢ"): env.get(bstack1ll11_opy_ (u"ࠦࡈࡌ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡑࡅࡒࡋࠢᴣ")),
            bstack1ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᴤ"): env.get(bstack1ll11_opy_ (u"ࠨࡃࡇࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᴥ"))
        }
    return {bstack1ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᴦ"): None}
def get_host_info():
    return {
        bstack1ll11_opy_ (u"ࠣࡪࡲࡷࡹࡴࡡ࡮ࡧࠥᴧ"): platform.node(),
        bstack1ll11_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦᴨ"): platform.system(),
        bstack1ll11_opy_ (u"ࠥࡸࡾࡶࡥࠣᴩ"): platform.machine(),
        bstack1ll11_opy_ (u"ࠦࡻ࡫ࡲࡴ࡫ࡲࡲࠧᴪ"): platform.version(),
        bstack1ll11_opy_ (u"ࠧࡧࡲࡤࡪࠥᴫ"): platform.architecture()[0]
    }
def bstack11l111ll1l_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111l1lll1l1_opy_():
    if bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧᴬ")):
        return bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᴭ")
    return bstack1ll11_opy_ (u"ࠨࡷࡱ࡯ࡳࡵࡷ࡯ࡡࡪࡶ࡮ࡪࠧᴮ")
def bstack111l1ll1lll_opy_(driver):
    info = {
        bstack1ll11_opy_ (u"ࠩࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨᴯ"): driver.capabilities,
        bstack1ll11_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠧᴰ"): driver.session_id,
        bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬᴱ"): driver.capabilities.get(bstack1ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪᴲ"), None),
        bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᴳ"): driver.capabilities.get(bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᴴ"), None),
        bstack1ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᴵ"): driver.capabilities.get(bstack1ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨᴶ"), None),
        bstack1ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ᴷ"):driver.capabilities.get(bstack1ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᴸ"), None),
    }
    if bstack111l1lll1l1_opy_() == bstack1ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᴹ"):
        if bstack1l1lllll11_opy_():
            info[bstack1ll11_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧᴺ")] = bstack1ll11_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᴻ")
        elif driver.capabilities.get(bstack1ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᴼ"), {}).get(bstack1ll11_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ᴽ"), False):
            info[bstack1ll11_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫᴾ")] = bstack1ll11_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨᴿ")
        else:
            info[bstack1ll11_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᵀ")] = bstack1ll11_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨᵁ")
    return info
def bstack1l1lllll11_opy_():
    if bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᵂ")):
        return True
    if bstack1llll1lll1_opy_(os.environ.get(bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩᵃ"), None)):
        return True
    return False
def bstack11ll1llll_opy_(bstack111l11lllll_opy_, url, data, config):
    headers = config.get(bstack1ll11_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪᵄ"), None)
    proxies = bstack1111l1ll1_opy_(config, url)
    auth = config.get(bstack1ll11_opy_ (u"ࠪࡥࡺࡺࡨࠨᵅ"), None)
    response = requests.request(
            bstack111l11lllll_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1l1lll1lll_opy_(bstack1l1lll11l_opy_, size):
    bstack1lll11l111_opy_ = []
    while len(bstack1l1lll11l_opy_) > size:
        bstack1llll1ll1l_opy_ = bstack1l1lll11l_opy_[:size]
        bstack1lll11l111_opy_.append(bstack1llll1ll1l_opy_)
        bstack1l1lll11l_opy_ = bstack1l1lll11l_opy_[size:]
    bstack1lll11l111_opy_.append(bstack1l1lll11l_opy_)
    return bstack1lll11l111_opy_
def bstack111ll11111l_opy_(message, bstack1111l1lll1l_opy_=False):
    os.write(1, bytes(message, bstack1ll11_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᵆ")))
    os.write(1, bytes(bstack1ll11_opy_ (u"ࠬࡢ࡮ࠨᵇ"), bstack1ll11_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᵈ")))
    if bstack1111l1lll1l_opy_:
        with open(bstack1ll11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠭ࡰ࠳࠴ࡽ࠲࠭ᵉ") + os.environ[bstack1ll11_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧᵊ")] + bstack1ll11_opy_ (u"ࠩ࠱ࡰࡴ࡭ࠧᵋ"), bstack1ll11_opy_ (u"ࠪࡥࠬᵌ")) as f:
            f.write(message + bstack1ll11_opy_ (u"ࠫࡡࡴࠧᵍ"))
def bstack1lll1ll1l1l_opy_():
    return os.environ[bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨᵎ")].lower() == bstack1ll11_opy_ (u"࠭ࡴࡳࡷࡨࠫᵏ")
def bstack1lll1111_opy_():
    return bstack1ll111ll_opy_().replace(tzinfo=None).isoformat() + bstack1ll11_opy_ (u"࡛ࠧࠩᵐ")
def bstack111l11l11ll_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack1ll11_opy_ (u"ࠨ࡜ࠪᵑ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack1ll11_opy_ (u"ࠩ࡝ࠫᵒ")))).total_seconds() * 1000
def bstack1111ll1lll1_opy_(timestamp):
    return bstack111l1ll1l1l_opy_(timestamp).isoformat() + bstack1ll11_opy_ (u"ࠪ࡞ࠬᵓ")
def bstack111l1lllll1_opy_(bstack1111lll1lll_opy_):
    date_format = bstack1ll11_opy_ (u"ࠫࠪ࡟ࠥ࡮ࠧࡧࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠴ࠥࡧࠩᵔ")
    bstack1111ll111l1_opy_ = datetime.datetime.strptime(bstack1111lll1lll_opy_, date_format)
    return bstack1111ll111l1_opy_.isoformat() + bstack1ll11_opy_ (u"ࠬࡠࠧᵕ")
def bstack1111ll1l11l_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack1ll11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᵖ")
    else:
        return bstack1ll11_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᵗ")
def bstack1llll1lll1_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack1ll11_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᵘ")
def bstack1111l1l1l1l_opy_(val):
    return val.__str__().lower() == bstack1ll11_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨᵙ")
def error_handler(bstack111l1l11l11_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111l1l11l11_opy_ as e:
                print(bstack1ll11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࢀࢃࠠ࠮ࡀࠣࡿࢂࡀࠠࡼࡿࠥᵚ").format(func.__name__, bstack111l1l11l11_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack111l11lll11_opy_(bstack111l11llll1_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack111l11llll1_opy_(cls, *args, **kwargs)
            except bstack111l1l11l11_opy_ as e:
                print(bstack1ll11_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࢁࡽࠡ࠯ࡁࠤࢀࢃ࠺ࠡࡽࢀࠦᵛ").format(bstack111l11llll1_opy_.__name__, bstack111l1l11l11_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack111l11lll11_opy_
    else:
        return decorator
def bstack111lll111l_opy_(bstack11l111ll_opy_):
    if os.getenv(bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨᵜ")) is not None:
        return bstack1llll1lll1_opy_(os.getenv(bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩᵝ")))
    if bstack1ll11_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᵞ") in bstack11l111ll_opy_ and bstack1111l1l1l1l_opy_(bstack11l111ll_opy_[bstack1ll11_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᵟ")]):
        return False
    if bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᵠ") in bstack11l111ll_opy_ and bstack1111l1l1l1l_opy_(bstack11l111ll_opy_[bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬᵡ")]):
        return False
    return True
def bstack11ll11lll1_opy_():
    try:
        from pytest_bdd import reporting
        bstack111l11l111l_opy_ = os.environ.get(bstack1ll11_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡙ࡘࡋࡒࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠦᵢ"), None)
        return bstack111l11l111l_opy_ is None or bstack111l11l111l_opy_ == bstack1ll11_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤᵣ")
    except Exception as e:
        return False
def bstack1ll1ll111l_opy_(hub_url, CONFIG):
    if bstack1llll1l1l1_opy_() <= version.parse(bstack1ll11_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ᵤ")):
        if hub_url:
            return bstack1ll11_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣᵥ") + hub_url + bstack1ll11_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧᵦ")
        return bstack1l1l1l111_opy_
    if hub_url:
        return bstack1ll11_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦᵧ") + hub_url + bstack1ll11_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦᵨ")
    return bstack1lll1l1l1l_opy_
def bstack1111lll1l1l_opy_():
    return isinstance(os.getenv(bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡑ࡛ࡇࡊࡐࠪᵩ")), str)
def bstack1l11lll11l_opy_(url):
    return urlparse(url).hostname
def bstack1lll111l11_opy_(hostname):
    for bstack11lll111l_opy_ in bstack1l11ll11l1_opy_:
        regex = re.compile(bstack11lll111l_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11ll11l1111_opy_(bstack111l1l1lll1_opy_, file_name, logger):
    bstack1l1llll11_opy_ = os.path.join(os.path.expanduser(bstack1ll11_opy_ (u"ࠬࢄࠧᵪ")), bstack111l1l1lll1_opy_)
    try:
        if not os.path.exists(bstack1l1llll11_opy_):
            os.makedirs(bstack1l1llll11_opy_)
        file_path = os.path.join(os.path.expanduser(bstack1ll11_opy_ (u"࠭ࡾࠨᵫ")), bstack111l1l1lll1_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack1ll11_opy_ (u"ࠧࡸࠩᵬ")):
                pass
            with open(file_path, bstack1ll11_opy_ (u"ࠣࡹ࠮ࠦᵭ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack111l111l1l_opy_.format(str(e)))
def bstack11ll111llll_opy_(file_name, key, value, logger):
    file_path = bstack11ll11l1111_opy_(bstack1ll11_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᵮ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack11l11111l1_opy_ = json.load(open(file_path, bstack1ll11_opy_ (u"ࠪࡶࡧ࠭ᵯ")))
        else:
            bstack11l11111l1_opy_ = {}
        bstack11l11111l1_opy_[key] = value
        with open(file_path, bstack1ll11_opy_ (u"ࠦࡼ࠱ࠢᵰ")) as outfile:
            json.dump(bstack11l11111l1_opy_, outfile)
def bstack1ll11ll1l1_opy_(file_name, logger):
    file_path = bstack11ll11l1111_opy_(bstack1ll11_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᵱ"), file_name, logger)
    bstack11l11111l1_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack1ll11_opy_ (u"࠭ࡲࠨᵲ")) as bstack1ll1ll1ll1_opy_:
            bstack11l11111l1_opy_ = json.load(bstack1ll1ll1ll1_opy_)
    return bstack11l11111l1_opy_
def bstack1l111l11l_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack1ll11_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡧࡩࡱ࡫ࡴࡪࡰࡪࠤ࡫࡯࡬ࡦ࠼ࠣࠫᵳ") + file_path + bstack1ll11_opy_ (u"ࠨࠢࠪᵴ") + str(e))
def bstack1llll1l1l1_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack1ll11_opy_ (u"ࠤ࠿ࡒࡔ࡚ࡓࡆࡖࡁࠦᵵ")
def bstack1lll111lll_opy_(config):
    if bstack1ll11_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᵶ") in config:
        del (config[bstack1ll11_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᵷ")])
        return False
    if bstack1llll1l1l1_opy_() < version.parse(bstack1ll11_opy_ (u"ࠬ࠹࠮࠵࠰࠳ࠫᵸ")):
        return False
    if bstack1llll1l1l1_opy_() >= version.parse(bstack1ll11_opy_ (u"࠭࠴࠯࠳࠱࠹ࠬᵹ")):
        return True
    if bstack1ll11_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧᵺ") in config and config[bstack1ll11_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨᵻ")] is False:
        return False
    else:
        return True
def bstack1111l11l1_opy_(args_list, bstack111l11ll1ll_opy_):
    index = -1
    for value in bstack111l11ll1ll_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack1111l1l1lll_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack1111l1l1lll_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1l1lllll_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1l1lllll_opy_ = bstack1l1lllll_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack1ll11_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᵼ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack1ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᵽ"), exception=exception)
    def bstack11111l111l_opy_(self):
        if self.result != bstack1ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᵾ"):
            return None
        if isinstance(self.exception_type, str) and bstack1ll11_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣᵿ") in self.exception_type:
            return bstack1ll11_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢᶀ")
        return bstack1ll11_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣᶁ")
    def bstack111l1l111ll_opy_(self):
        if self.result != bstack1ll11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᶂ"):
            return None
        if self.bstack1l1lllll_opy_:
            return self.bstack1l1lllll_opy_
        return bstack1111lllll11_opy_(self.exception)
def bstack1111lllll11_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack1111ll11ll1_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1ll1ll11_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack11lll11l11_opy_(config, logger):
    try:
        import playwright
        bstack111l1l11l1l_opy_ = playwright.__file__
        bstack111l111ll1l_opy_ = os.path.split(bstack111l1l11l1l_opy_)
        bstack111l11l11l1_opy_ = bstack111l111ll1l_opy_[0] + bstack1ll11_opy_ (u"ࠩ࠲ࡨࡷ࡯ࡶࡦࡴ࠲ࡴࡦࡩ࡫ࡢࡩࡨ࠳ࡱ࡯ࡢ࠰ࡥ࡯࡭࠴ࡩ࡬ࡪ࠰࡭ࡷࠬᶃ")
        os.environ[bstack1ll11_opy_ (u"ࠪࡋࡑࡕࡂࡂࡎࡢࡅࡌࡋࡎࡕࡡࡋࡘ࡙ࡖ࡟ࡑࡔࡒ࡜࡞࠭ᶄ")] = bstack11l1l11l11_opy_(config)
        with open(bstack111l11l11l1_opy_, bstack1ll11_opy_ (u"ࠫࡷ࠭ᶅ")) as f:
            file_content = f.read()
            bstack111l1l1111l_opy_ = bstack1ll11_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠫᶆ")
            bstack111ll1111l1_opy_ = file_content.find(bstack111l1l1111l_opy_)
            if bstack111ll1111l1_opy_ == -1:
              process = subprocess.Popen(bstack1ll11_opy_ (u"ࠨ࡮ࡱ࡯ࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠥᶇ"), shell=True, cwd=bstack111l111ll1l_opy_[0])
              process.wait()
              bstack111l11l1l1l_opy_ = bstack1ll11_opy_ (u"ࠧࠣࡷࡶࡩࠥࡹࡴࡳ࡫ࡦࡸࠧࡁࠧᶈ")
              bstack111l111l111_opy_ = bstack1ll11_opy_ (u"ࠣࠤࠥࠤࡡࠨࡵࡴࡧࠣࡷࡹࡸࡩࡤࡶ࡟ࠦࡀࠦࡣࡰࡰࡶࡸࠥࢁࠠࡣࡱࡲࡸࡸࡺࡲࡢࡲࠣࢁࠥࡃࠠࡳࡧࡴࡹ࡮ࡸࡥࠩࠩࡪࡰࡴࡨࡡ࡭࠯ࡤ࡫ࡪࡴࡴࠨࠫ࠾ࠤ࡮࡬ࠠࠩࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡨࡲࡻ࠴ࡇࡍࡑࡅࡅࡑࡥࡁࡈࡇࡑࡘࡤࡎࡔࡕࡒࡢࡔࡗࡕࡘ࡚ࠫࠣࡦࡴࡵࡴࡴࡶࡵࡥࡵ࠮ࠩ࠼ࠢࠥࠦࠧᶉ")
              bstack111l111lll1_opy_ = file_content.replace(bstack111l11l1l1l_opy_, bstack111l111l111_opy_)
              with open(bstack111l11l11l1_opy_, bstack1ll11_opy_ (u"ࠩࡺࠫᶊ")) as f:
                f.write(bstack111l111lll1_opy_)
    except Exception as e:
        logger.error(bstack111llllll_opy_.format(str(e)))
def bstack111l1l1ll_opy_():
  try:
    bstack111l11l1111_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll11_opy_ (u"ࠪࡳࡵࡺࡩ࡮ࡣ࡯ࡣ࡭ࡻࡢࡠࡷࡵࡰ࠳ࡰࡳࡰࡰࠪᶋ"))
    bstack1111l1l1ll1_opy_ = []
    if os.path.exists(bstack111l11l1111_opy_):
      with open(bstack111l11l1111_opy_) as f:
        bstack1111l1l1ll1_opy_ = json.load(f)
      os.remove(bstack111l11l1111_opy_)
    return bstack1111l1l1ll1_opy_
  except:
    pass
  return []
def bstack1111ll1l1_opy_(bstack1l1111ll11_opy_):
  try:
    bstack1111l1l1ll1_opy_ = []
    bstack111l11l1111_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll11_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠴ࡪࡴࡱࡱࠫᶌ"))
    if os.path.exists(bstack111l11l1111_opy_):
      with open(bstack111l11l1111_opy_) as f:
        bstack1111l1l1ll1_opy_ = json.load(f)
    bstack1111l1l1ll1_opy_.append(bstack1l1111ll11_opy_)
    with open(bstack111l11l1111_opy_, bstack1ll11_opy_ (u"ࠬࡽࠧᶍ")) as f:
        json.dump(bstack1111l1l1ll1_opy_, f)
  except:
    pass
def bstack11ll1lllll_opy_(logger, bstack111l11ll111_opy_ = False):
  try:
    test_name = os.environ.get(bstack1ll11_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩᶎ"), bstack1ll11_opy_ (u"ࠧࠨᶏ"))
    if test_name == bstack1ll11_opy_ (u"ࠨࠩᶐ"):
        test_name = threading.current_thread().__dict__.get(bstack1ll11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡄࡧࡨࡤࡺࡥࡴࡶࡢࡲࡦࡳࡥࠨᶑ"), bstack1ll11_opy_ (u"ࠪࠫᶒ"))
    bstack111l1l1ll11_opy_ = bstack1ll11_opy_ (u"ࠫ࠱ࠦࠧᶓ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack111l11ll111_opy_:
        bstack111l111lll_opy_ = os.environ.get(bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬᶔ"), bstack1ll11_opy_ (u"࠭࠰ࠨᶕ"))
        bstack1ll11ll1ll_opy_ = {bstack1ll11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᶖ"): test_name, bstack1ll11_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᶗ"): bstack111l1l1ll11_opy_, bstack1ll11_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨᶘ"): bstack111l111lll_opy_}
        bstack1111l1lllll_opy_ = []
        bstack1111ll1llll_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡴࡵࡶ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩᶙ"))
        if os.path.exists(bstack1111ll1llll_opy_):
            with open(bstack1111ll1llll_opy_) as f:
                bstack1111l1lllll_opy_ = json.load(f)
        bstack1111l1lllll_opy_.append(bstack1ll11ll1ll_opy_)
        with open(bstack1111ll1llll_opy_, bstack1ll11_opy_ (u"ࠫࡼ࠭ᶚ")) as f:
            json.dump(bstack1111l1lllll_opy_, f)
    else:
        bstack1ll11ll1ll_opy_ = {bstack1ll11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᶛ"): test_name, bstack1ll11_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᶜ"): bstack111l1l1ll11_opy_, bstack1ll11_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ᶝ"): str(multiprocessing.current_process().name)}
        if bstack1ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸࠬᶞ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1ll11ll1ll_opy_)
  except Exception as e:
      logger.warn(bstack1ll11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡵࡿࡴࡦࡵࡷࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢ࠼ࠣࡿࢂࠨᶟ").format(e))
def bstack111l11lll1_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1ll11_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠥࡴ࡯ࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥࡨࡡࡴ࡫ࡦࠤ࡫࡯࡬ࡦࠢࡲࡴࡪࡸࡡࡵ࡫ࡲࡲࡸ࠭ᶠ"))
    try:
      bstack111l111l1ll_opy_ = []
      bstack1ll11ll1ll_opy_ = {bstack1ll11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᶡ"): test_name, bstack1ll11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᶢ"): error_message, bstack1ll11_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᶣ"): index}
      bstack1111l1ll111_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll11_opy_ (u"ࠧࡳࡱࡥࡳࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨᶤ"))
      if os.path.exists(bstack1111l1ll111_opy_):
          with open(bstack1111l1ll111_opy_) as f:
              bstack111l111l1ll_opy_ = json.load(f)
      bstack111l111l1ll_opy_.append(bstack1ll11ll1ll_opy_)
      with open(bstack1111l1ll111_opy_, bstack1ll11_opy_ (u"ࠨࡹࠪᶥ")) as f:
          json.dump(bstack111l111l1ll_opy_, f)
    except Exception as e:
      logger.warn(bstack1ll11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡷࡵࡢࡰࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧᶦ").format(e))
    return
  bstack111l111l1ll_opy_ = []
  bstack1ll11ll1ll_opy_ = {bstack1ll11_opy_ (u"ࠪࡲࡦࡳࡥࠨᶧ"): test_name, bstack1ll11_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᶨ"): error_message, bstack1ll11_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᶩ"): index}
  bstack1111l1ll111_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll11_opy_ (u"࠭ࡲࡰࡤࡲࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧᶪ"))
  lock_file = bstack1111l1ll111_opy_ + bstack1ll11_opy_ (u"ࠧ࠯࡮ࡲࡧࡰ࠭ᶫ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1111l1ll111_opy_):
          with open(bstack1111l1ll111_opy_, bstack1ll11_opy_ (u"ࠨࡴࠪᶬ")) as f:
              content = f.read().strip()
              if content:
                  bstack111l111l1ll_opy_ = json.load(open(bstack1111l1ll111_opy_))
      bstack111l111l1ll_opy_.append(bstack1ll11ll1ll_opy_)
      with open(bstack1111l1ll111_opy_, bstack1ll11_opy_ (u"ࠩࡺࠫᶭ")) as f:
          json.dump(bstack111l111l1ll_opy_, f)
  except Exception as e:
    logger.warn(bstack1ll11_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡸ࡯ࡣࡱࡷࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡧ࡫࡯ࡩࠥࡲ࡯ࡤ࡭࡬ࡲ࡬ࡀࠠࡼࡿࠥᶮ").format(e))
def bstack1111l11ll1_opy_(bstack1111l1ll11_opy_, name, logger):
  try:
    bstack1ll11ll1ll_opy_ = {bstack1ll11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᶯ"): name, bstack1ll11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᶰ"): bstack1111l1ll11_opy_, bstack1ll11_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᶱ"): str(threading.current_thread()._name)}
    return bstack1ll11ll1ll_opy_
  except Exception as e:
    logger.warn(bstack1ll11_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡥࡩ࡭ࡧࡶࡦࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧ࠺ࠡࡽࢀࠦᶲ").format(e))
  return
def bstack111ll1111ll_opy_():
    return platform.system() == bstack1ll11_opy_ (u"ࠨ࡙࡬ࡲࡩࡵࡷࡴࠩᶳ")
def bstack1l1l1lll11_opy_(bstack111l1l11111_opy_, config, logger):
    bstack111l1lll11l_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack111l1l11111_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack1ll11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡭ࡶࡨࡶࠥࡩ࡯࡯ࡨ࡬࡫ࠥࡱࡥࡺࡵࠣࡦࡾࠦࡲࡦࡩࡨࡼࠥࡳࡡࡵࡥ࡫࠾ࠥࢁࡽࠣᶴ").format(e))
    return bstack111l1lll11l_opy_
def bstack11l1ll1ll1l_opy_(bstack111l1l1ll1l_opy_, bstack111l1lll111_opy_):
    bstack1111l1ll1ll_opy_ = version.parse(bstack111l1l1ll1l_opy_)
    bstack111l1lll1ll_opy_ = version.parse(bstack111l1lll111_opy_)
    if bstack1111l1ll1ll_opy_ > bstack111l1lll1ll_opy_:
        return 1
    elif bstack1111l1ll1ll_opy_ < bstack111l1lll1ll_opy_:
        return -1
    else:
        return 0
def bstack1ll111ll_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack111l1ll1l1l_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack1111ll1l111_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack111llll1ll_opy_(options, framework, config, bstack11llll1ll1_opy_={}):
    if options is None:
        return
    if getattr(options, bstack1ll11_opy_ (u"ࠪ࡫ࡪࡺࠧᶵ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1ll1lll1l_opy_ = caps.get(bstack1ll11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᶶ"))
    bstack111l1l1l1ll_opy_ = True
    bstack11lll1ll11_opy_ = os.environ[bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᶷ")]
    bstack1l1111ll11l_opy_ = config.get(bstack1ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᶸ"), False)
    if bstack1l1111ll11l_opy_:
        bstack1l1l1l111ll_opy_ = config.get(bstack1ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᶹ"), {})
        bstack1l1l1l111ll_opy_[bstack1ll11_opy_ (u"ࠨࡣࡸࡸ࡭࡚࡯࡬ࡧࡱࠫᶺ")] = os.getenv(bstack1ll11_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧᶻ"))
        bstack1111lll111l_opy_ = json.loads(os.getenv(bstack1ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫᶼ"), bstack1ll11_opy_ (u"ࠫࢀࢃࠧᶽ"))).get(bstack1ll11_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᶾ"))
    if bstack1111l1l1l1l_opy_(caps.get(bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦ࡙࠶ࡇࠬᶿ"))) or bstack1111l1l1l1l_opy_(caps.get(bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡵࡴࡧࡢࡻ࠸ࡩࠧ᷀"))):
        bstack111l1l1l1ll_opy_ = False
    if bstack1lll111lll_opy_({bstack1ll11_opy_ (u"ࠣࡷࡶࡩ࡜࠹ࡃࠣ᷁"): bstack111l1l1l1ll_opy_}):
        bstack1ll1lll1l_opy_ = bstack1ll1lll1l_opy_ or {}
        bstack1ll1lll1l_opy_[bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎ᷂ࠫ")] = bstack1111ll1l111_opy_(framework)
        bstack1ll1lll1l_opy_[bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ᷃")] = bstack1lll1ll1l1l_opy_()
        bstack1ll1lll1l_opy_[bstack1ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧ᷄")] = bstack11lll1ll11_opy_
        bstack1ll1lll1l_opy_[bstack1ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧ᷅")] = bstack11llll1ll1_opy_
        if bstack1l1111ll11l_opy_:
            bstack1ll1lll1l_opy_[bstack1ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭᷆")] = bstack1l1111ll11l_opy_
            bstack1ll1lll1l_opy_[bstack1ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ᷇")] = bstack1l1l1l111ll_opy_
            bstack1ll1lll1l_opy_[bstack1ll11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ᷈")][bstack1ll11_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ᷉")] = bstack1111lll111l_opy_
        if getattr(options, bstack1ll11_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼ᷊ࠫ"), None):
            options.set_capability(bstack1ll11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ᷋"), bstack1ll1lll1l_opy_)
        else:
            options[bstack1ll11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭᷌")] = bstack1ll1lll1l_opy_
    else:
        if getattr(options, bstack1ll11_opy_ (u"࠭ࡳࡦࡶࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹࡿࠧ᷍"), None):
            options.set_capability(bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨ᷎"), bstack1111ll1l111_opy_(framework))
            options.set_capability(bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯᷏ࠩ"), bstack1lll1ll1l1l_opy_())
            options.set_capability(bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧ᷐ࠫ"), bstack11lll1ll11_opy_)
            options.set_capability(bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫ᷑"), bstack11llll1ll1_opy_)
            if bstack1l1111ll11l_opy_:
                options.set_capability(bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ᷒"), bstack1l1111ll11l_opy_)
                options.set_capability(bstack1ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᷓ"), bstack1l1l1l111ll_opy_)
                options.set_capability(bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷ࠳ࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᷔ"), bstack1111lll111l_opy_)
        else:
            options[bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨᷕ")] = bstack1111ll1l111_opy_(framework)
            options[bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᷖ")] = bstack1lll1ll1l1l_opy_()
            options[bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫᷗ")] = bstack11lll1ll11_opy_
            options[bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫᷘ")] = bstack11llll1ll1_opy_
            if bstack1l1111ll11l_opy_:
                options[bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᷙ")] = bstack1l1111ll11l_opy_
                options[bstack1ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫᷚ")] = bstack1l1l1l111ll_opy_
                options[bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᷛ")][bstack1ll11_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨᷜ")] = bstack1111lll111l_opy_
    return options
def bstack1111l1l11l1_opy_(ws_endpoint, framework):
    bstack11llll1ll1_opy_ = bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"ࠣࡒࡏࡅ࡞࡝ࡒࡊࡉࡋࡘࡤࡖࡒࡐࡆࡘࡇ࡙ࡥࡍࡂࡒࠥᷝ"))
    if ws_endpoint and len(ws_endpoint.split(bstack1ll11_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨᷞ"))) > 1:
        ws_url = ws_endpoint.split(bstack1ll11_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩᷟ"))[0]
        if bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧᷠ") in ws_url:
            from browserstack_sdk._version import __version__
            bstack1111ll1ll11_opy_ = json.loads(urllib.parse.unquote(ws_endpoint.split(bstack1ll11_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫᷡ"))[1]))
            bstack1111ll1ll11_opy_ = bstack1111ll1ll11_opy_ or {}
            bstack11lll1ll11_opy_ = os.environ[bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᷢ")]
            bstack1111ll1ll11_opy_[bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨᷣ")] = str(framework) + str(__version__)
            bstack1111ll1ll11_opy_[bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩᷤ")] = bstack1lll1ll1l1l_opy_()
            bstack1111ll1ll11_opy_[bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫᷥ")] = bstack11lll1ll11_opy_
            bstack1111ll1ll11_opy_[bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫᷦ")] = bstack11llll1ll1_opy_
            ws_endpoint = ws_endpoint.split(bstack1ll11_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪᷧ"))[0] + bstack1ll11_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫᷨ") + urllib.parse.quote(json.dumps(bstack1111ll1ll11_opy_))
    return ws_endpoint
def bstack11l11l1ll_opy_():
    global bstack1ll1lll1l1_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1ll1lll1l1_opy_ = BrowserType.connect
    return bstack1ll1lll1l1_opy_
def bstack1lll11l1ll_opy_(framework_name):
    global bstack1l111llll_opy_
    bstack1l111llll_opy_ = framework_name
    return framework_name
def bstack111ll1l11l_opy_(self, *args, **kwargs):
    global bstack1ll1lll1l1_opy_
    try:
        global bstack1l111llll_opy_
        if bstack1ll11_opy_ (u"࠭ࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶࠪᷩ") in kwargs:
            kwargs[bstack1ll11_opy_ (u"ࠧࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷࠫᷪ")] = bstack1111l1l11l1_opy_(
                kwargs.get(bstack1ll11_opy_ (u"ࠨࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸࠬᷫ"), None),
                bstack1l111llll_opy_
            )
    except Exception as e:
        logger.error(bstack1ll11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫ࡩࡳࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡗࡉࡑࠠࡤࡣࡳࡷ࠿ࠦࡻࡾࠤᷬ").format(str(e)))
    return bstack1ll1lll1l1_opy_(self, *args, **kwargs)
def bstack1111l1l11ll_opy_(bstack111l111llll_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack1111l1ll1_opy_(bstack111l111llll_opy_, bstack1ll11_opy_ (u"ࠥࠦᷭ"))
        if proxies and proxies.get(bstack1ll11_opy_ (u"ࠦ࡭ࡺࡴࡱࡵࠥᷮ")):
            parsed_url = urlparse(proxies.get(bstack1ll11_opy_ (u"ࠧ࡮ࡴࡵࡲࡶࠦᷯ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack1ll11_opy_ (u"࠭ࡰࡳࡱࡻࡽࡍࡵࡳࡵࠩᷰ")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack1ll11_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖ࡯ࡳࡶࠪᷱ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack1ll11_opy_ (u"ࠨࡲࡵࡳࡽࡿࡕࡴࡧࡵࠫᷲ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack1ll11_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡣࡶࡷࠬᷳ")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack1ll1l11lll_opy_(bstack111l111llll_opy_):
    bstack111l1l1llll_opy_ = {
        bstack11l1l1l11ll_opy_[bstack1111ll1l1l1_opy_]: bstack111l111llll_opy_[bstack1111ll1l1l1_opy_]
        for bstack1111ll1l1l1_opy_ in bstack111l111llll_opy_
        if bstack1111ll1l1l1_opy_ in bstack11l1l1l11ll_opy_
    }
    bstack111l1l1llll_opy_[bstack1ll11_opy_ (u"ࠥࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵࠥᷴ")] = bstack1111l1l11ll_opy_(bstack111l111llll_opy_, bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"ࠦࡵࡸ࡯ࡹࡻࡖࡩࡹࡺࡩ࡯ࡩࡶࠦ᷵")))
    bstack111l11l1l11_opy_ = [element.lower() for element in bstack11l11ll1l1l_opy_]
    bstack1111ll1l1ll_opy_(bstack111l1l1llll_opy_, bstack111l11l1l11_opy_)
    return bstack111l1l1llll_opy_
def bstack1111ll1l1ll_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack1ll11_opy_ (u"ࠧ࠰ࠪࠫࠬࠥ᷶")
    for value in d.values():
        if isinstance(value, dict):
            bstack1111ll1l1ll_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack1111ll1l1ll_opy_(item, keys)
def bstack1ll11l1l111_opy_():
    bstack1111llll11l_opy_ = [os.environ.get(bstack1ll11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡉࡍࡇࡖࡣࡉࡏࡒ᷷ࠣ")), os.path.join(os.path.expanduser(bstack1ll11_opy_ (u"ࠢࡿࠤ᷸")), bstack1ll11_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ᷹")), os.path.join(bstack1ll11_opy_ (u"ࠩ࠲ࡸࡲࡶ᷺ࠧ"), bstack1ll11_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ᷻"))]
    for path in bstack1111llll11l_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack1ll11_opy_ (u"ࠦࡋ࡯࡬ࡦࠢࠪࠦ᷼") + str(path) + bstack1ll11_opy_ (u"ࠧ࠭ࠠࡦࡺ࡬ࡷࡹࡹ࠮᷽ࠣ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack1ll11_opy_ (u"ࠨࡇࡪࡸ࡬ࡲ࡬ࠦࡰࡦࡴࡰ࡭ࡸࡹࡩࡰࡰࡶࠤ࡫ࡵࡲࠡࠩࠥ᷾") + str(path) + bstack1ll11_opy_ (u"ࠢࠨࠤ᷿"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack1ll11_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࠧࠣḀ") + str(path) + bstack1ll11_opy_ (u"ࠤࠪࠤࡦࡲࡲࡦࡣࡧࡽࠥ࡮ࡡࡴࠢࡷ࡬ࡪࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡤࠡࡲࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲࡸ࠴ࠢḁ"))
            else:
                logger.debug(bstack1ll11_opy_ (u"ࠥࡇࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧࠣࠫࠧḂ") + str(path) + bstack1ll11_opy_ (u"ࠦࠬࠦࡷࡪࡶ࡫ࠤࡼࡸࡩࡵࡧࠣࡴࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴ࠮ࠣḃ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack1ll11_opy_ (u"ࠧࡕࡰࡦࡴࡤࡸ࡮ࡵ࡮ࠡࡵࡸࡧࡨ࡫ࡥࡥࡧࡧࠤ࡫ࡵࡲࠡࠩࠥḄ") + str(path) + bstack1ll11_opy_ (u"ࠨࠧ࠯ࠤḅ"))
            return path
        except Exception as e:
            logger.debug(bstack1ll11_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡶࡲࠣࡪ࡮ࡲࡥࠡࠩࡾࡴࡦࡺࡨࡾࠩ࠽ࠤࠧḆ") + str(e) + bstack1ll11_opy_ (u"ࠣࠤḇ"))
    logger.debug(bstack1ll11_opy_ (u"ࠤࡄࡰࡱࠦࡰࡢࡶ࡫ࡷࠥ࡬ࡡࡪ࡮ࡨࡨ࠳ࠨḈ"))
    return None
@measure(event_name=EVENTS.bstack11l1l1lllll_opy_, stage=STAGE.bstack1111l1111_opy_)
def bstack1l1ll111111_opy_(binary_path, bstack1l1l1llll11_opy_, bs_config):
    logger.debug(bstack1ll11_opy_ (u"ࠥࡇࡺࡸࡲࡦࡰࡷࠤࡈࡒࡉࠡࡒࡤࡸ࡭ࠦࡦࡰࡷࡱࡨ࠿ࠦࡻࡾࠤḉ").format(binary_path))
    bstack111l11111l1_opy_ = bstack1ll11_opy_ (u"ࠫࠬḊ")
    bstack1111lll1l11_opy_ = {
        bstack1ll11_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪḋ"): __version__,
        bstack1ll11_opy_ (u"ࠨ࡯ࡴࠤḌ"): platform.system(),
        bstack1ll11_opy_ (u"ࠢࡰࡵࡢࡥࡷࡩࡨࠣḍ"): platform.machine(),
        bstack1ll11_opy_ (u"ࠣࡥ࡯࡭ࡤࡼࡥࡳࡵ࡬ࡳࡳࠨḎ"): bstack1ll11_opy_ (u"ࠩ࠳ࠫḏ"),
        bstack1ll11_opy_ (u"ࠥࡷࡩࡱ࡟࡭ࡣࡱ࡫ࡺࡧࡧࡦࠤḐ"): bstack1ll11_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫḑ")
    }
    bstack1111ll11l1l_opy_(bstack1111lll1l11_opy_)
    try:
        if binary_path:
            bstack1111lll1l11_opy_[bstack1ll11_opy_ (u"ࠬࡩ࡬ࡪࡡࡹࡩࡷࡹࡩࡰࡰࠪḒ")] = subprocess.check_output([binary_path, bstack1ll11_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢḓ")]).strip().decode(bstack1ll11_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭Ḕ"))
        response = requests.request(
            bstack1ll11_opy_ (u"ࠨࡉࡈࡘࠬḕ"),
            url=bstack111lll1ll_opy_(bstack11l1l1ll11l_opy_),
            headers=None,
            auth=(bs_config[bstack1ll11_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫḖ")], bs_config[bstack1ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ḗ")]),
            json=None,
            params=bstack1111lll1l11_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack1ll11_opy_ (u"ࠫࡺࡸ࡬ࠨḘ") in data.keys() and bstack1ll11_opy_ (u"ࠬࡻࡰࡥࡣࡷࡩࡩࡥࡣ࡭࡫ࡢࡺࡪࡸࡳࡪࡱࡱࠫḙ") in data.keys():
            logger.debug(bstack1ll11_opy_ (u"ࠨࡎࡦࡧࡧࠤࡹࡵࠠࡶࡲࡧࡥࡹ࡫ࠠࡣ࡫ࡱࡥࡷࡿࠬࠡࡥࡸࡶࡷ࡫࡮ࡵࠢࡥ࡭ࡳࡧࡲࡺࠢࡹࡩࡷࡹࡩࡰࡰ࠽ࠤࢀࢃࠢḚ").format(bstack1111lll1l11_opy_[bstack1ll11_opy_ (u"ࠧࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬḛ")]))
            if bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡖࡔࡏࠫḜ") in os.environ:
                logger.debug(bstack1ll11_opy_ (u"ࠤࡖ࡯࡮ࡶࡰࡪࡰࡪࠤࡧ࡯࡮ࡢࡴࡼࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡡࡴࠢࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡗࡕࡐࠥ࡯ࡳࠡࡵࡨࡸࠧḝ"))
                data[bstack1ll11_opy_ (u"ࠪࡹࡷࡲࠧḞ")] = os.environ[bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢ࡙ࡗࡒࠧḟ")]
            bstack111l11lll1l_opy_ = bstack1111ll11lll_opy_(data[bstack1ll11_opy_ (u"ࠬࡻࡲ࡭ࠩḠ")], bstack1l1l1llll11_opy_)
            bstack111l11111l1_opy_ = os.path.join(bstack1l1l1llll11_opy_, bstack111l11lll1l_opy_)
            os.chmod(bstack111l11111l1_opy_, 0o777) # bstack111l1l11ll1_opy_ permission
            return bstack111l11111l1_opy_
    except Exception as e:
        logger.debug(bstack1ll11_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡱࡩࡼࠦࡓࡅࡍࠣࡿࢂࠨḡ").format(e))
    return binary_path
def bstack1111ll11l1l_opy_(bstack1111lll1l11_opy_):
    try:
        if bstack1ll11_opy_ (u"ࠧ࡭࡫ࡱࡹࡽ࠭Ḣ") not in bstack1111lll1l11_opy_[bstack1ll11_opy_ (u"ࠨࡱࡶࠫḣ")].lower():
            return
        if os.path.exists(bstack1ll11_opy_ (u"ࠤ࠲ࡩࡹࡩ࠯ࡰࡵ࠰ࡶࡪࡲࡥࡢࡵࡨࠦḤ")):
            with open(bstack1ll11_opy_ (u"ࠥ࠳ࡪࡺࡣ࠰ࡱࡶ࠱ࡷ࡫࡬ࡦࡣࡶࡩࠧḥ"), bstack1ll11_opy_ (u"ࠦࡷࠨḦ")) as f:
                bstack1111ll11l11_opy_ = {}
                for line in f:
                    if bstack1ll11_opy_ (u"ࠧࡃࠢḧ") in line:
                        key, value = line.rstrip().split(bstack1ll11_opy_ (u"ࠨ࠽ࠣḨ"), 1)
                        bstack1111ll11l11_opy_[key] = value.strip(bstack1ll11_opy_ (u"ࠧࠣ࡞ࠪࠫḩ"))
                bstack1111lll1l11_opy_[bstack1ll11_opy_ (u"ࠨࡦ࡬ࡷࡹࡸ࡯ࠨḪ")] = bstack1111ll11l11_opy_.get(bstack1ll11_opy_ (u"ࠤࡌࡈࠧḫ"), bstack1ll11_opy_ (u"ࠥࠦḬ"))
        elif os.path.exists(bstack1ll11_opy_ (u"ࠦ࠴࡫ࡴࡤ࠱ࡤࡰࡵ࡯࡮ࡦ࠯ࡵࡩࡱ࡫ࡡࡴࡧࠥḭ")):
            bstack1111lll1l11_opy_[bstack1ll11_opy_ (u"ࠬࡪࡩࡴࡶࡵࡳࠬḮ")] = bstack1ll11_opy_ (u"࠭ࡡ࡭ࡲ࡬ࡲࡪ࠭ḯ")
    except Exception as e:
        logger.debug(bstack1ll11_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡺࠠࡥ࡫ࡶࡸࡷࡵࠠࡰࡨࠣࡰ࡮ࡴࡵࡹࠤḰ") + e)
@measure(event_name=EVENTS.bstack11l1l1ll1ll_opy_, stage=STAGE.bstack1111l1111_opy_)
def bstack1111ll11lll_opy_(bstack111l1ll1111_opy_, bstack1111llll1ll_opy_):
    logger.debug(bstack1ll11_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡷࡵ࡭࠻ࠢࠥḱ") + str(bstack111l1ll1111_opy_) + bstack1ll11_opy_ (u"ࠤࠥḲ"))
    zip_path = os.path.join(bstack1111llll1ll_opy_, bstack1ll11_opy_ (u"ࠥࡨࡴࡽ࡮࡭ࡱࡤࡨࡪࡪ࡟ࡧ࡫࡯ࡩ࠳ࢀࡩࡱࠤḳ"))
    bstack111l11lll1l_opy_ = bstack1ll11_opy_ (u"ࠫࠬḴ")
    with requests.get(bstack111l1ll1111_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack1ll11_opy_ (u"ࠧࡽࡢࠣḵ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack1ll11_opy_ (u"ࠨࡆࡪ࡮ࡨࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿ࠮ࠣḶ"))
    with zipfile.ZipFile(zip_path, bstack1ll11_opy_ (u"ࠧࡳࠩḷ")) as zip_ref:
        bstack1111lllll1l_opy_ = zip_ref.namelist()
        if len(bstack1111lllll1l_opy_) > 0:
            bstack111l11lll1l_opy_ = bstack1111lllll1l_opy_[0] # bstack111l1111lll_opy_ bstack11l1l11llll_opy_ will be bstack1111l1l1l11_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack1111llll1ll_opy_)
        logger.debug(bstack1ll11_opy_ (u"ࠣࡈ࡬ࡰࡪࡹࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾࠦࡥࡹࡶࡵࡥࡨࡺࡥࡥࠢࡷࡳࠥ࠭ࠢḸ") + str(bstack1111llll1ll_opy_) + bstack1ll11_opy_ (u"ࠤࠪࠦḹ"))
    os.remove(zip_path)
    return bstack111l11lll1l_opy_
def get_cli_dir():
    bstack111l1111ll1_opy_ = bstack1ll11l1l111_opy_()
    if bstack111l1111ll1_opy_:
        bstack1l1l1llll11_opy_ = os.path.join(bstack111l1111ll1_opy_, bstack1ll11_opy_ (u"ࠥࡧࡱ࡯ࠢḺ"))
        if not os.path.exists(bstack1l1l1llll11_opy_):
            os.makedirs(bstack1l1l1llll11_opy_, mode=0o777, exist_ok=True)
        return bstack1l1l1llll11_opy_
    else:
        raise FileNotFoundError(bstack1ll11_opy_ (u"ࠦࡓࡵࠠࡸࡴ࡬ࡸࡦࡨ࡬ࡦࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡨࡲࡶࠥࡺࡨࡦࠢࡖࡈࡐࠦࡢࡪࡰࡤࡶࡾ࠴ࠢḻ"))
def bstack1l1l1l1ll11_opy_(bstack1l1l1llll11_opy_):
    bstack1ll11_opy_ (u"ࠧࠨࠢࡈࡧࡷࠤࡹ࡮ࡥࠡࡲࡤࡸ࡭ࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡓࡅࡍࠣࡦ࡮ࡴࡡࡳࡻࠣ࡭ࡳࠦࡡࠡࡹࡵ࡭ࡹࡧࡢ࡭ࡧࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾ࠴ࠢࠣࠤḼ")
    bstack1111l1ll1l1_opy_ = [
        os.path.join(bstack1l1l1llll11_opy_, f)
        for f in os.listdir(bstack1l1l1llll11_opy_)
        if os.path.isfile(os.path.join(bstack1l1l1llll11_opy_, f)) and f.startswith(bstack1ll11_opy_ (u"ࠨࡢࡪࡰࡤࡶࡾ࠳ࠢḽ"))
    ]
    if len(bstack1111l1ll1l1_opy_) > 0:
        return max(bstack1111l1ll1l1_opy_, key=os.path.getmtime) # get bstack1111l1ll11l_opy_ binary
    return bstack1ll11_opy_ (u"ࠢࠣḾ")
def bstack111l11ll1l1_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l111l1ll1l_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1l111l1ll1l_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack11l11111l_opy_(data, keys, default=None):
    bstack1ll11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡕࡤࡪࡪࡲࡹࠡࡩࡨࡸࠥࡧࠠ࡯ࡧࡶࡸࡪࡪࠠࡷࡣ࡯ࡹࡪࠦࡦࡳࡱࡰࠤࡦࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳࡻࠣࡳࡷࠦ࡬ࡪࡵࡷ࠲ࠏࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢࡧࡥࡹࡧ࠺ࠡࡖ࡫ࡩࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺࠢࡲࡶࠥࡲࡩࡴࡶࠣࡸࡴࠦࡴࡳࡣࡹࡩࡷࡹࡥ࠯ࠌࠣࠤࠥࠦ࠺ࡱࡣࡵࡥࡲࠦ࡫ࡦࡻࡶ࠾ࠥࡇࠠ࡭࡫ࡶࡸࠥࡵࡦࠡ࡭ࡨࡽࡸ࠵ࡩ࡯ࡦ࡬ࡧࡪࡹࠠࡳࡧࡳࡶࡪࡹࡥ࡯ࡶ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡴࡦࡺࡨ࠯ࠌࠣࠤࠥࠦ࠺ࡱࡣࡵࡥࡲࠦࡤࡦࡨࡤࡹࡱࡺ࠺ࠡࡘࡤࡰࡺ࡫ࠠࡵࡱࠣࡶࡪࡺࡵࡳࡰࠣ࡭࡫ࠦࡴࡩࡧࠣࡴࡦࡺࡨࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠰ࠍࠤࠥࠦࠠ࠻ࡴࡨࡸࡺࡸ࡮࠻ࠢࡗ࡬ࡪࠦࡶࡢ࡮ࡸࡩࠥࡧࡴࠡࡶ࡫ࡩࠥࡴࡥࡴࡶࡨࡨࠥࡶࡡࡵࡪ࠯ࠤࡴࡸࠠࡥࡧࡩࡥࡺࡲࡴࠡ࡫ࡩࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪ࠮ࠋࠢࠣࠤࠥࠨࠢࠣḿ")
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