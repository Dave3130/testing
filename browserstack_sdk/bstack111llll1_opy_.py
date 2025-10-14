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
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack111l1lll_opy_
import subprocess
import re
from browserstack_sdk.bstack1llllllll_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack111l11ll_opy_
from bstack_utils.bstack1llll11l1_opy_ import bstack11l1l111_opy_
from bstack_utils.constants import bstack11111111_opy_
from bstack_utils.bstack11l111ll_opy_ import bstack1lll1ll1l_opy_
class bstack11111l11_opy_:
    bstack11111l1l_opy_ = bstack11l1l11_opy_ (u"ࡲࠨ࠾ࡐࡳࡩࡻ࡬ࡦࠢࠫ࡟ࡣࡄ࡝ࠬࠫࡁࠫ঒")  # bstack1lll1lll1_opy_ lines bstack1llllll1_opy_ <Module path/to/bstack1llll1l1l_opy_.py> in pytest --collect-bstack1lllll1l1_opy_ output
    def __init__(self, args, logger, bstack111ll1ll_opy_, bstack111l1l1l_opy_):
        self.args = args
        self.logger = logger
        self.bstack111ll1ll_opy_ = bstack111ll1ll_opy_
        self.bstack111l1l1l_opy_ = bstack111l1l1l_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack11l11lll_opy_ = []
        self.bstack111ll111_opy_ = []
        self.bstack11l11111_opy_ = []
        self.bstack1llll111l_opy_ = self.bstack111ll11l_opy_()
        self.bstack11l11l11_opy_ = -1
    def bstack1llllll11_opy_(self, bstack111l1l11_opy_):
        self.parse_args()
        self.bstack1111111l_opy_()
        self.bstack1llllll1l_opy_(bstack111l1l11_opy_)
        self.bstack1111llll_opy_()
    def bstack111l1ll1_opy_(self):
        bstack11l111ll_opy_ = bstack1lll1ll1l_opy_.bstack1111lll1_opy_(self.bstack111ll1ll_opy_, self.logger)
        if bstack11l111ll_opy_ is None:
            self.logger.warn(bstack11l1l11_opy_ (u"ࠣࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡪࡤࡲࡩࡲࡥࡳࠢ࡬ࡷࠥࡴ࡯ࡵࠢ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡪ࠮ࠡࡕ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦও"))
            return
        bstack11l111l1_opy_ = False
        bstack11l111ll_opy_.bstack111l11l1_opy_(bstack11l1l11_opy_ (u"ࠤࡨࡲࡦࡨ࡬ࡦࡦࠥঔ"), bstack11l111ll_opy_.bstack1lllll11l_opy_())
        start_time = time.time()
        if bstack11l111ll_opy_.bstack1lllll11l_opy_():
            test_files = self.bstack111lll11_opy_()
            bstack11l111l1_opy_ = True
            bstack111111l1_opy_ = bstack11l111ll_opy_.bstack111lllll_opy_(test_files)
            if bstack111111l1_opy_:
                self.bstack11l11lll_opy_ = [os.path.normpath(item).replace(bstack11l1l11_opy_ (u"ࠪࡠࡡ࠭ক"), bstack11l1l11_opy_ (u"ࠫ࠴࠭খ")) for item in bstack111111l1_opy_]
                self.__1lll1ll11_opy_()
                bstack11l111ll_opy_.bstack1111l1l1_opy_(bstack11l111l1_opy_)
                self.logger.info(bstack11l1l11_opy_ (u"࡚ࠧࡥࡴࡶࡶࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡶࡵ࡬ࡲ࡬ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡀࠠࡼࡿࠥগ").format(self.bstack11l11lll_opy_))
            else:
                self.logger.info(bstack11l1l11_opy_ (u"ࠨࡎࡰࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡷࡦࡴࡨࠤࡷ࡫࡯ࡳࡦࡨࡶࡪࡪࠠࡣࡻࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦঘ"))
        bstack11l111ll_opy_.bstack111l11l1_opy_(bstack11l1l11_opy_ (u"ࠢࡵ࡫ࡰࡩ࡙ࡧ࡫ࡦࡰࡗࡳࡆࡶࡰ࡭ࡻࠥঙ"), int((time.time() - start_time) * 1000)) # bstack1llll1ll1_opy_ to bstack11l1l11l_opy_
    def __1lll1ll11_opy_(self):
        bstack11l1l11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡌ࡯ࡳࠢࡨࡥࡨ࡮ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡳࡦ࡮ࡩ࠲ࡸࡶࡥࡤࡡࡩ࡭ࡱ࡫ࡳ࠭ࠢࡦࡳࡱࡲࡥࡤࡶࠣࡥࡱࡲࠠ࡯ࡱࡧࡩ࡮ࡪࡳࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠠ࠮࠯ࡦࡳࡱࡲࡥࡤࡶ࠰ࡳࡳࡲࡹࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧচ")
        bstack1llll1l11_opy_ = []
        for bstack1llll1l1l_opy_ in self.bstack11l11lll_opy_:
            bstack1111l111_opy_ = [bstack11l1l11_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵࠤছ"), bstack1llll1l1l_opy_, bstack11l1l11_opy_ (u"ࠥ࠱࠲ࡩ࡯࡭࡮ࡨࡧࡹ࠳࡯࡯࡮ࡼࠦজ"), bstack11l1l11_opy_ (u"ࠦ࠲ࡷࠢঝ")]
            result = subprocess.run(bstack1111l111_opy_, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.stderr:
                self.logger.info(bstack11l1l11_opy_ (u"ࠧ࡝ࡡࡳࡰ࡬ࡲ࡬ࡹࠠࡥࡷࡵ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯࠼ࠣࡿࢂࠨঞ").format(result.stderr))
            if result.returncode != 0 and not result.stdout:
                self.logger.error(bstack11l1l11_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࡹ࠺ࠡࡽࢀࠦট").format(result.stderr))
                continue
            for line in result.stdout.splitlines():
                line = line.strip()
                if line and not line.startswith(bstack11l1l11_opy_ (u"ࠢ࠽ࠤঠ")) and bstack11l1l11_opy_ (u"ࠣ࠼࠽ࠦড") in line:
                    bstack1llll1l11_opy_.append(line)
        os.environ[bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡑࡕࡇࡍࡋࡓࡕࡔࡄࡘࡊࡊ࡟ࡔࡇࡏࡉࡈ࡚ࡏࡓࡕࠪঢ")] = json.dumps(bstack1llll1l11_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack11l1111l_opy_():
        import importlib
        if getattr(importlib, bstack11l1l11_opy_ (u"ࠪࡪ࡮ࡴࡤࡠ࡮ࡲࡥࡩ࡫ࡲࠨণ"), False):
            bstack111lll1l_opy_ = importlib.find_loader(bstack11l1l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭ত"))
        else:
            bstack111lll1l_opy_ = importlib.util.find_spec(bstack11l1l11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧথ"))
    def bstack111l111l_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack11l11l11_opy_ = -1
        if self.bstack111l1l1l_opy_ and bstack11l1l11_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭দ") in self.bstack111ll1ll_opy_:
            self.bstack11l11l11_opy_ = int(self.bstack111ll1ll_opy_[bstack11l1l11_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧধ")])
        try:
            bstack1llll1lll_opy_ = [bstack11l1l11_opy_ (u"ࠨ࠯࠰ࡨࡷ࡯ࡶࡦࡴࠪন"), bstack11l1l11_opy_ (u"ࠩ࠰࠱ࡵࡲࡵࡨ࡫ࡱࡷࠬ঩"), bstack11l1l11_opy_ (u"ࠪ࠱ࡵ࠭প")]
            if self.bstack11l11l11_opy_ >= 0:
                bstack1llll1lll_opy_.extend([bstack11l1l11_opy_ (u"ࠫ࠲࠳࡮ࡶ࡯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬফ"), bstack11l1l11_opy_ (u"ࠬ࠳࡮ࠨব")])
            for arg in bstack1llll1lll_opy_:
                self.bstack111l111l_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack1111111l_opy_(self):
        bstack111ll111_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack111ll111_opy_ = bstack111ll111_opy_
        return self.bstack111ll111_opy_
    def bstack1111ll11_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack11l1111l_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack111l11ll_opy_)
    def bstack1llllll1l_opy_(self, bstack111l1l11_opy_):
        bstack111111ll_opy_ = Config.bstack1111lll1_opy_()
        if bstack111l1l11_opy_:
            self.bstack111ll111_opy_.append(bstack11l1l11_opy_ (u"࠭࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪভ"))
            self.bstack111ll111_opy_.append(bstack11l1l11_opy_ (u"ࠧࡕࡴࡸࡩࠬম"))
        if bstack111111ll_opy_.bstack11l11ll1_opy_():
            self.bstack111ll111_opy_.append(bstack11l1l11_opy_ (u"ࠨ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧয"))
            self.bstack111ll111_opy_.append(bstack11l1l11_opy_ (u"ࠩࡗࡶࡺ࡫ࠧর"))
        self.bstack111ll111_opy_.append(bstack11l1l11_opy_ (u"ࠪ࠱ࡵ࠭঱"))
        self.bstack111ll111_opy_.append(bstack11l1l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡳࡰࡺ࡭ࡩ࡯ࠩল"))
        self.bstack111ll111_opy_.append(bstack11l1l11_opy_ (u"ࠬ࠳࠭ࡥࡴ࡬ࡺࡪࡸࠧ঳"))
        self.bstack111ll111_opy_.append(bstack11l1l11_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭঴"))
        if self.bstack11l11l11_opy_ > 1:
            self.bstack111ll111_opy_.append(bstack11l1l11_opy_ (u"ࠧ࠮ࡰࠪ঵"))
            self.bstack111ll111_opy_.append(str(self.bstack11l11l11_opy_))
    def bstack1111llll_opy_(self):
        if bstack11l1l111_opy_.bstack1lll1l1ll_opy_(self.bstack111ll1ll_opy_):
             self.bstack111ll111_opy_ += [
                bstack11111111_opy_.get(bstack11l1l11_opy_ (u"ࠨࡴࡨࡶࡺࡴࠧশ")), str(bstack11l1l111_opy_.bstack1lllll111_opy_(self.bstack111ll1ll_opy_)),
                bstack11111111_opy_.get(bstack11l1l11_opy_ (u"ࠩࡧࡩࡱࡧࡹࠨষ")), str(bstack11111111_opy_.get(bstack11l1l11_opy_ (u"ࠪࡶࡪࡸࡵ࡯࠯ࡧࡩࡱࡧࡹࠨস")))
            ]
    def bstack1lllllll1_opy_(self):
        bstack11l11111_opy_ = []
        for spec in self.bstack11l11lll_opy_:
            bstack1111l1ll_opy_ = [spec]
            bstack1111l1ll_opy_ += self.bstack111ll111_opy_
            bstack11l11111_opy_.append(bstack1111l1ll_opy_)
        self.bstack11l11111_opy_ = bstack11l11111_opy_
        return bstack11l11111_opy_
    def bstack111ll11l_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1llll111l_opy_ = True
            return True
        except Exception as e:
            self.bstack1llll111l_opy_ = False
        return self.bstack1llll111l_opy_
    def bstack1111l11l_opy_(self):
        bstack11l1l11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡍࡥࡵࠢࡷ࡬ࡪࠦࡣࡰࡷࡱࡸࠥࡵࡦࠡࡶࡨࡷࡹࡹࠠࡸ࡫ࡷ࡬ࡴࡻࡴࠡࡴࡸࡲࡳ࡯࡮ࡨࠢࡷ࡬ࡪࡳࠠࡶࡵ࡬ࡲ࡬ࠦࡰࡺࡶࡨࡷࡹ࠭ࡳࠡ࠯࠰ࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡴࡴ࡬ࡺࠢࡩࡰࡦ࡭࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࡭ࡳࡺ࠺ࠡࡖ࡫ࡩࠥࡺ࡯ࡵࡣ࡯ࠤࡳࡻ࡭ࡣࡧࡵࠤࡴ࡬ࠠࡵࡧࡶࡸࡸࠦࡣࡰ࡮࡯ࡩࡨࡺࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢহ")
        try:
            self.logger.info(bstack11l1l11_opy_ (u"ࠧࡉ࡯࡭࡮ࡨࡧࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࡳࠡࡷࡶ࡭ࡳ࡭ࠠࡱࡻࡷࡩࡸࡺࠠ࠮࠯ࡦࡳࡱࡲࡥࡤࡶ࠰ࡳࡳࡲࡹࠣ঺"))
            bstack1111l111_opy_ = [bstack11l1l11_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨ঻"), *self.bstack111ll111_opy_, bstack11l1l11_opy_ (u"ࠢ࠮࠯ࡦࡳࡱࡲࡥࡤࡶ࠰ࡳࡳࡲࡹ়ࠣ")]
            result = subprocess.run(bstack1111l111_opy_, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.stderr:
                self.logger.info(bstack11l1l11_opy_ (u"࡙ࠣࡤࡶࡳ࡯࡮ࡨࡵࠣࡨࡺࡸࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡥࡲࡹࡳࡺࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱ࠾ࠥࢁࡽࠣঽ").format(result.stderr))
            if result.returncode != 0 and not result.stdout:
                self.logger.error(bstack11l1l11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡻ࡮ࡵ࠼ࠣࡿࢂࠨা").format(result.stderr))
                return 0
            test_count = result.stdout.count(bstack11l1l11_opy_ (u"ࠥࡀࡋࡻ࡮ࡤࡶ࡬ࡳࡳࠦࠢি"))
            self.logger.info(bstack11l1l11_opy_ (u"࡙ࠦࡵࡴࡢ࡮ࠣࡸࡪࡹࡴࡴࠢࡦࡳࡱࡲࡥࡤࡶࡨࡨ࠿ࠦࡻࡾࠤী").format(test_count))
            return test_count
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡣࡰࡷࡱࡸ࠿ࠦࡻࡾࠤু").format(e))
            return 0
    def bstack1llll11ll_opy_(self, bstack11111lll_opy_, bstack1llllll11_opy_):
        bstack1llllll11_opy_[bstack11l1l11_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭ূ")] = self.bstack111ll1ll_opy_
        multiprocessing.set_start_method(bstack11l1l11_opy_ (u"ࠧࡴࡲࡤࡻࡳ࠭ৃ"))
        bstack1lll1llll_opy_ = []
        manager = multiprocessing.Manager()
        bstack111ll1l1_opy_ = manager.list()
        if bstack11l1l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫৄ") in self.bstack111ll1ll_opy_:
            for index, platform in enumerate(self.bstack111ll1ll_opy_[bstack11l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ৅")]):
                bstack1lll1llll_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack11111lll_opy_,
                                                            args=(self.bstack111ll111_opy_, bstack1llllll11_opy_, bstack111ll1l1_opy_)))
            bstack1lllll1ll_opy_ = len(self.bstack111ll1ll_opy_[bstack11l1l11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭৆")])
        else:
            bstack1lll1llll_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack11111lll_opy_,
                                                        args=(self.bstack111ll111_opy_, bstack1llllll11_opy_, bstack111ll1l1_opy_)))
            bstack1lllll1ll_opy_ = 1
        i = 0
        for t in bstack1lll1llll_opy_:
            os.environ[bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫে")] = str(i)
            if bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨৈ") in self.bstack111ll1ll_opy_:
                os.environ[bstack11l1l11_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧ৉")] = json.dumps(self.bstack111ll1ll_opy_[bstack11l1l11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ৊")][i % bstack1lllll1ll_opy_])
            i += 1
            t.start()
        for t in bstack1lll1llll_opy_:
            t.join()
        return list(bstack111ll1l1_opy_)
    @staticmethod
    def bstack11111ll1_opy_(driver, bstack111l1111_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack11l1l11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬো"), None)
        if item and getattr(item, bstack11l1l11_opy_ (u"ࠩࡢࡥ࠶࠷ࡹࡠࡶࡨࡷࡹࡥࡣࡢࡵࡨࠫৌ"), None) and not getattr(item, bstack11l1l11_opy_ (u"ࠪࡣࡦ࠷࠱ࡺࡡࡶࡸࡴࡶ࡟ࡥࡱࡱࡩ্ࠬ"), False):
            logger.info(
                bstack11l1l11_opy_ (u"ࠦࡆࡻࡴࡰ࡯ࡤࡸࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠥ࡮ࡡࡴࠢࡨࡲࡩ࡫ࡤ࠯ࠢࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡮ࡹࠠࡶࡰࡧࡩࡷࡽࡡࡺ࠰ࠥৎ"))
            bstack1111ll1l_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack111l1lll_opy_.bstack11l11l1l_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack111lll11_opy_(self):
        bstack11l1l11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵࠣࡸ࡭࡫ࠠ࡭࡫ࡶࡸࠥࡵࡦࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡺ࡯ࠡࡤࡨࠤࡪࡾࡥࡤࡷࡷࡩࡩࠦࡢࡺࠢࡳࡥࡷࡹࡩ࡯ࡩࠣࡸ࡭࡫ࠠࡰࡷࡷࡴࡺࡺࠠࡰࡨࠣࡴࡾࡺࡥࡴࡶࠣ࠱࠲ࡩ࡯࡭࡮ࡨࡧࡹ࠳࡯࡯࡮ࡼ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡎࡰࡶࡨ࠾࡚ࠥࡨࡦࠢࡵࡩ࡬࡫ࡸࠡࡲࡤࡸࡹ࡫ࡲ࡯ࠢࡸࡷࡪࡪࠠࡩࡧࡵࡩࠥࡪࡥࡱࡧࡱࡨࡸࠦ࡯࡯ࠢࡳࡽࡹ࡫ࡳࡵࠩࡶࠤࡴࡻࡴࡱࡷࡷࠤ࡫ࡵࡲ࡮ࡣࡷࠤ࡫ࡵࡲࠡ࠾ࡐࡳࡩࡻ࡬ࡦࠢ࠱࠲࠳ࡄࠠ࡭࡫ࡱࡩࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ৏")
        try:
            bstack1111l111_opy_ = [bstack11l1l11_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࠨ৐"), *self.bstack111ll111_opy_, bstack11l1l11_opy_ (u"ࠢ࠮࠯ࡦࡳࡱࡲࡥࡤࡶ࠰ࡳࡳࡲࡹࠣ৑")]
            result = subprocess.run(bstack1111l111_opy_, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.stderr:
                self.logger.info(bstack11l1l11_opy_ (u"࡙ࠣࡤࡶࡳ࡯࡮ࡨࡵࠣࡨࡺࡸࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱ࠾ࠥࢁࡽࠣ৒").format(result.stderr))
            if result.returncode != 0 and not result.stdout:
                self.logger.error(bstack11l1l11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࡵࠣࡪ࡮ࡲࡥ࠻ࠢࡾࢁࠧ৓").format(result.stderr))
                return []
            file_names = set(re.findall(self.bstack11111l1l_opy_, result.stdout))
            file_names = sorted(file_names)
            return list(file_names)
        except Exception as e:
            self.logger.error(bstack1llll1111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࡀࠠࡼࡧࢀࠦ৔"))
            return []