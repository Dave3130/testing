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
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack11l11lll_opy_
import subprocess
import re
from browserstack_sdk.bstack111lll11_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l11l11_opy_
from bstack_utils.bstack1lll1ll1l_opy_ import bstack11l11l1l_opy_
from bstack_utils.constants import bstack11l11111_opy_
from bstack_utils.bstack1llllll1l_opy_ import bstack1llll1l1l_opy_
class bstack111l11l1_opy_:
    def __init__(self, args, logger, bstack11l111ll_opy_, bstack11l11ll1_opy_):
        self.args = args
        self.logger = logger
        self.bstack11l111ll_opy_ = bstack11l111ll_opy_
        self.bstack11l11ll1_opy_ = bstack11l11ll1_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack111l111l_opy_ = []
        self.bstack1111111l_opy_ = []
        self.bstack1111l111_opy_ = []
        self.bstack1lllllll1_opy_ = self.bstack111l1111_opy_()
        self.bstack1lllll11l_opy_ = -1
    def bstack11111ll1_opy_(self, bstack1llll1111_opy_):
        self.parse_args()
        self.bstack111111ll_opy_()
        self.bstack111ll1l1_opy_(bstack1llll1111_opy_)
        self.bstack111l1lll_opy_()
    def bstack111ll111_opy_(self):
        bstack1llllll1l_opy_ = bstack1llll1l1l_opy_.bstack1llll11l1_opy_(self.bstack11l111ll_opy_, self.logger)
        if bstack1llllll1l_opy_ is None:
            self.logger.warn(bstack1ll11_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡩࡣࡱࡨࡱ࡫ࡲࠡ࡫ࡶࠤࡳࡵࡴࠡ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡩ࠴ࠠࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥ঒"))
            return
        bstack1111l1ll_opy_ = False
        bstack1llllll1l_opy_.bstack1llll11ll_opy_(bstack1ll11_opy_ (u"ࠣࡧࡱࡥࡧࡲࡥࡥࠤও"), bstack1llllll1l_opy_.bstack1lllll111_opy_())
        start_time = time.time()
        if bstack1llllll1l_opy_.bstack1lllll111_opy_():
            test_files = self.bstack1111l1l1_opy_()
            bstack1111l1ll_opy_ = True
            bstack1llllllll_opy_ = bstack1llllll1l_opy_.bstack11111l11_opy_(test_files)
            if bstack1llllllll_opy_:
                self.bstack111l111l_opy_ = [os.path.normpath(item).replace(bstack1ll11_opy_ (u"ࠩ࡟ࡠࠬঔ"), bstack1ll11_opy_ (u"ࠪ࠳ࠬক")) for item in bstack1llllllll_opy_]
                self.__1llllll11_opy_()
                bstack1llllll1l_opy_.bstack11l1l111_opy_(bstack1111l1ll_opy_)
                self.logger.info(bstack1ll11_opy_ (u"࡙ࠦ࡫ࡳࡵࡵࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡵࡴ࡫ࡱ࡫ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤখ").format(self.bstack111l111l_opy_))
            else:
                self.logger.info(bstack1ll11_opy_ (u"ࠧࡔ࡯ࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡽࡥࡳࡧࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡢࡺࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥগ"))
        bstack1llllll1l_opy_.bstack1llll11ll_opy_(bstack1ll11_opy_ (u"ࠨࡴࡪ࡯ࡨࡘࡦࡱࡥ࡯ࡖࡲࡅࡵࡶ࡬ࡺࠤঘ"), int((time.time() - start_time) * 1000)) # bstack111ll11l_opy_ to bstack11111l1l_opy_
    def __1llllll11_opy_(self):
        bstack1ll11_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡋࡵࡲࠡࡧࡤࡧ࡭ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࠢ࡬ࡲࠥࡹࡥ࡭ࡨ࠱ࡷࡵ࡫ࡣࡠࡨ࡬ࡰࡪࡹࠬࠡࡥࡲࡰࡱ࡫ࡣࡵࠢࡤࡰࡱࠦ࡮ࡰࡦࡨ࡭ࡩࡹࠠࡶࡵ࡬ࡲ࡬ࠦࡰࡺࡶࡨࡷࡹࠦ࠭࠮ࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡲࡲࡱࡿࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦঙ")
        bstack111ll1ll_opy_ = []
        for bstack11111lll_opy_ in self.bstack111l111l_opy_:
            try:
                bstack1llll1ll1_opy_ = [bstack1ll11_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣচ"), bstack11111lll_opy_, bstack1ll11_opy_ (u"ࠤ࠰࠱ࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡵ࡮࡭ࡻࠥছ"), bstack1ll11_opy_ (u"ࠥ࠱ࡶࠨজ")]
                result = subprocess.run(bstack1llll1ll1_opy_, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if result.returncode != 0 and result.stdout:
                    self.logger.error(bstack1ll11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡳ࡭ࠠ࡯ࡱࡧࡩࠥ࡯ࡤࠡࡨࡲࡶࠥࢁࡽ࠻ࠢࡾࢁࠧঝ").format(bstack11111lll_opy_, result.stderr))
                    continue
                for line in result.stdout.splitlines():
                    line = line.strip()
                    if line and not line.startswith(bstack1ll11_opy_ (u"ࠧࡂࠢঞ")) and bstack1ll11_opy_ (u"ࠨ࠺࠻ࠤট") in line:
                        bstack111ll1ll_opy_.append(line)
            except Exception as e:
                self.logger.error(bstack1ll11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡲࡴࡪࡥࠡ࡫ࡧࠤ࡫ࡵࡲࠡࡨ࡬ࡰࡪࡀࠠࡼࡿࠥঠ").format(bstack11111lll_opy_))
                return 0
        os.environ[bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡐࡔࡆࡌࡊ࡙ࡔࡓࡃࡗࡉࡉࡥࡓࡆࡎࡈࡇ࡙ࡕࡒࡔࠩড")] = json.dumps(bstack111ll1ll_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack111l1ll1_opy_():
        import importlib
        if getattr(importlib, bstack1ll11_opy_ (u"ࠩࡩ࡭ࡳࡪ࡟࡭ࡱࡤࡨࡪࡸࠧঢ"), False):
            bstack1lllll1l1_opy_ = importlib.find_loader(bstack1ll11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠬণ"))
        else:
            bstack1lllll1l1_opy_ = importlib.util.find_spec(bstack1ll11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭ত"))
    def bstack11l111l1_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1lllll11l_opy_ = -1
        if self.bstack11l11ll1_opy_ and bstack1ll11_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬথ") in self.bstack11l111ll_opy_:
            self.bstack1lllll11l_opy_ = int(self.bstack11l111ll_opy_[bstack1ll11_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭দ")])
        try:
            bstack111l11ll_opy_ = [bstack1ll11_opy_ (u"ࠧ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠩধ"), bstack1ll11_opy_ (u"ࠨ࠯࠰ࡴࡱࡻࡧࡪࡰࡶࠫন"), bstack1ll11_opy_ (u"ࠩ࠰ࡴࠬ঩")]
            if self.bstack1lllll11l_opy_ >= 0:
                bstack111l11ll_opy_.extend([bstack1ll11_opy_ (u"ࠪ࠱࠲ࡴࡵ࡮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫপ"), bstack1ll11_opy_ (u"ࠫ࠲ࡴࠧফ")])
            for arg in bstack111l11ll_opy_:
                self.bstack11l111l1_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack111111ll_opy_(self):
        bstack1111111l_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1111111l_opy_ = bstack1111111l_opy_
        return self.bstack1111111l_opy_
    def bstack1llll1l11_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack111l1ll1_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack11l11l11_opy_)
    def bstack111ll1l1_opy_(self, bstack1llll1111_opy_):
        bstack1111ll11_opy_ = Config.bstack1llll11l1_opy_()
        if bstack1llll1111_opy_:
            self.bstack1111111l_opy_.append(bstack1ll11_opy_ (u"ࠬ࠳࠭ࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩব"))
            self.bstack1111111l_opy_.append(bstack1ll11_opy_ (u"࠭ࡔࡳࡷࡨࠫভ"))
        if bstack1111ll11_opy_.bstack1111l11l_opy_():
            self.bstack1111111l_opy_.append(bstack1ll11_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ম"))
            self.bstack1111111l_opy_.append(bstack1ll11_opy_ (u"ࠨࡖࡵࡹࡪ࠭য"))
        self.bstack1111111l_opy_.append(bstack1ll11_opy_ (u"ࠩ࠰ࡴࠬর"))
        self.bstack1111111l_opy_.append(bstack1ll11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡲ࡯ࡹ࡬࡯࡮ࠨ঱"))
        self.bstack1111111l_opy_.append(bstack1ll11_opy_ (u"ࠫ࠲࠳ࡤࡳ࡫ࡹࡩࡷ࠭ল"))
        self.bstack1111111l_opy_.append(bstack1ll11_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ঳"))
        if self.bstack1lllll11l_opy_ > 1:
            self.bstack1111111l_opy_.append(bstack1ll11_opy_ (u"࠭࠭࡯ࠩ঴"))
            self.bstack1111111l_opy_.append(str(self.bstack1lllll11l_opy_))
    def bstack111l1lll_opy_(self):
        if bstack11l11l1l_opy_.bstack11111111_opy_(self.bstack11l111ll_opy_):
             self.bstack1111111l_opy_ += [
                bstack11l11111_opy_.get(bstack1ll11_opy_ (u"ࠧࡳࡧࡵࡹࡳ࠭঵")), str(bstack11l11l1l_opy_.bstack111lllll_opy_(self.bstack11l111ll_opy_)),
                bstack11l11111_opy_.get(bstack1ll11_opy_ (u"ࠨࡦࡨࡰࡦࡿࠧশ")), str(bstack11l11111_opy_.get(bstack1ll11_opy_ (u"ࠩࡵࡩࡷࡻ࡮࠮ࡦࡨࡰࡦࡿࠧষ")))
            ]
    def bstack1lll1lll1_opy_(self):
        bstack1111l111_opy_ = []
        for spec in self.bstack111l111l_opy_:
            bstack11l1l11l_opy_ = [spec]
            bstack11l1l11l_opy_ += self.bstack1111111l_opy_
            bstack1111l111_opy_.append(bstack11l1l11l_opy_)
        self.bstack1111l111_opy_ = bstack1111l111_opy_
        return bstack1111l111_opy_
    def bstack111l1111_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack1lllllll1_opy_ = True
            return True
        except Exception as e:
            self.bstack1lllllll1_opy_ = False
        return self.bstack1lllllll1_opy_
    def bstack1111llll_opy_(self):
        bstack1ll11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡌ࡫ࡴࠡࡶ࡫ࡩࠥࡩ࡯ࡶࡰࡷࠤࡴ࡬ࠠࡵࡧࡶࡸࡸࠦࡷࡪࡶ࡫ࡳࡺࡺࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡶ࡫ࡩࡲࠦࡵࡴ࡫ࡱ࡫ࠥࡶࡹࡵࡧࡶࡸࠬࡹࠠ࠮࠯ࡦࡳࡱࡲࡥࡤࡶ࠰ࡳࡳࡲࡹࠡࡨ࡯ࡥ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡲࡹࡀࠠࡕࡪࡨࠤࡹࡵࡴࡢ࡮ࠣࡲࡺࡳࡢࡦࡴࠣࡳ࡫ࠦࡴࡦࡵࡷࡷࠥࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨস")
        try:
            self.logger.info(bstack1ll11_opy_ (u"ࠦࡈࡵ࡬࡭ࡧࡦࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࡹࠠࡶࡵ࡬ࡲ࡬ࠦࡰࡺࡶࡨࡷࡹࠦ࠭࠮ࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡲࡲࡱࡿࠢহ"))
            bstack1llll1ll1_opy_ = [bstack1ll11_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࠧ঺"), *self.bstack1111111l_opy_, bstack1ll11_opy_ (u"ࠨ࠭࠮ࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡲࡲࡱࡿࠢ঻"), bstack1ll11_opy_ (u"ࠢ࠮ࡳ়ࠥ")]
            result = subprocess.run(
                bstack1llll1ll1_opy_,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if result.returncode not in (0, 5) and result.stdout:
                self.logger.error(bstack1ll11_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡣࡰ࡮࡯ࡩࡨࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࡴ࠼ࠣࡿࢂࠨঽ").format(result.stderr))
                return 0
            test_count = 0
            for line in result.stdout.splitlines():
                line = line.strip()
                if line and bstack1ll11_opy_ (u"ࠩ࠽࠾ࠬা") in line and not line.startswith(bstack1ll11_opy_ (u"ࠪࡀࠬি")) and not line.endswith(bstack1ll11_opy_ (u"ࠫࡨࡵ࡬࡭ࡧࡦࡸࡪࡪࠧী")):
                    test_count += 1
            self.logger.info(bstack1ll11_opy_ (u"࡚ࠧ࡯ࡵࡣ࡯ࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡲ࡬ࡦࡥࡷࡩࡩࡀࠠࡼࡿࠥু").format(test_count))
            return test_count
        except Exception as e:
            self.logger.error(bstack1ll11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤࡱࡸࡲࡹࡀࠠࡼࡿࠥূ").format(e))
            return 0
    def bstack1llll1lll_opy_(self, bstack111llll1_opy_, bstack11111ll1_opy_):
        bstack11111ll1_opy_[bstack1ll11_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧৃ")] = self.bstack11l111ll_opy_
        multiprocessing.set_start_method(bstack1ll11_opy_ (u"ࠨࡵࡳࡥࡼࡴࠧৄ"))
        bstack11l1111l_opy_ = []
        manager = multiprocessing.Manager()
        bstack111l1l11_opy_ = manager.list()
        if bstack1ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ৅") in self.bstack11l111ll_opy_:
            for index, platform in enumerate(self.bstack11l111ll_opy_[bstack1ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭৆")]):
                bstack11l1111l_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack111llll1_opy_,
                                                            args=(self.bstack1111111l_opy_, bstack11111ll1_opy_, bstack111l1l11_opy_)))
            bstack1llll111l_opy_ = len(self.bstack11l111ll_opy_[bstack1ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧে")])
        else:
            bstack11l1111l_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack111llll1_opy_,
                                                        args=(self.bstack1111111l_opy_, bstack11111ll1_opy_, bstack111l1l11_opy_)))
            bstack1llll111l_opy_ = 1
        i = 0
        for t in bstack11l1111l_opy_:
            os.environ[bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬৈ")] = str(i)
            if bstack1ll11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৉") in self.bstack11l111ll_opy_:
                os.environ[bstack1ll11_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨ৊")] = json.dumps(self.bstack11l111ll_opy_[bstack1ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫো")][i % bstack1llll111l_opy_])
            i += 1
            t.start()
        for t in bstack11l1111l_opy_:
            t.join()
        return list(bstack111l1l11_opy_)
    @staticmethod
    def bstack1111ll1l_opy_(driver, bstack111lll1l_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack1ll11_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭ৌ"), None)
        if item and getattr(item, bstack1ll11_opy_ (u"ࠪࡣࡦ࠷࠱ࡺࡡࡷࡩࡸࡺ࡟ࡤࡣࡶࡩ্ࠬ"), None) and not getattr(item, bstack1ll11_opy_ (u"ࠫࡤࡧ࠱࠲ࡻࡢࡷࡹࡵࡰࡠࡦࡲࡲࡪ࠭ৎ"), False):
            logger.info(
                bstack1ll11_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠣࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡯ࡳࠡࡷࡱࡨࡪࡸࡷࡢࡻ࠱ࠦ৏"))
            bstack1111lll1_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack11l11lll_opy_.bstack1lllll1ll_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack1111l1l1_opy_(self):
        bstack1ll11_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶࠤࡹ࡮ࡥࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡴࡰࠢࡥࡩࠥ࡫ࡸࡦࡥࡸࡸࡪࡪࠠࡣࡻࠣࡴࡦࡸࡳࡪࡰࡪࠤࡹ࡮ࡥࠡࡱࡸࡸࡵࡻࡴࠡࡱࡩࠤࡵࡿࡴࡦࡵࡷࠤ࠲࠳ࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡰࡰ࡯ࡽ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ৐")
        try:
            bstack1llll1ll1_opy_ = [
                bstack1ll11_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺࠢ৑"),
                *self.bstack1111111l_opy_,
                bstack1ll11_opy_ (u"ࠣ࠯࠰ࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡴࡴ࡬ࡺࠤ৒"),
                bstack1ll11_opy_ (u"ࠤ࠰ࡵࠧ৓")  # bstack111111l1_opy_ mode for bstack111l1l1l_opy_ output
            ]
            result = subprocess.run(
                bstack1llll1ll1_opy_,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            if result.returncode not in (0, 5) and result.stdout:
                self.logger.error(bstack1ll11_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࡶࠤ࡫࡯࡬ࡦ࠼ࠣࡿࢂ࠭৔").format(result.stderr))
                return []
            file_paths = set()
            for line in result.stdout.splitlines():
                line = line.strip()
                if line and bstack1ll11_opy_ (u"ࠫ࠿ࡀࠧ৕") in line and not line.startswith(bstack1ll11_opy_ (u"ࠬࡂࠧ৖")):
                    file_path = line.split(bstack1ll11_opy_ (u"࠭࠺࠻ࠩৗ"), 1)[0]
                    if file_path.endswith(bstack1ll11_opy_ (u"ࠧ࠯ࡲࡼࠫ৘")):
                        file_paths.add(file_path)
            test_files = sorted(file_paths)
            if test_files:
                self.logger.debug(bstack1ll11_opy_ (u"ࠣࡅࡲࡰࡱ࡫ࡣࡵࡧࡧࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳ࠻ࠢࡾࢁࠧ৙").format(len(test_files)))
            elif result.returncode == 5:
                self.logger.debug(bstack1ll11_opy_ (u"ࠤࡑࡳࠥࡺࡥࡴࡶࡶࠤ࡫࡯࡬ࡦࡵࠣࡧࡴࡲ࡬ࡦࡥࡷࡩࡩࠨ৚"))
            return test_files
        except Exception as e:
            self.logger.error(bstack1ll11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࡀࠠࡼࡿࠥ৛").format(e))
            return []