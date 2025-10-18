# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack1lll1ll1l_opy_
from browserstack_sdk.bstack11l1111l_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l11l11_opy_
from bstack_utils.bstack11l111l1_opy_ import bstack1111llll_opy_
from bstack_utils.constants import bstack11111l11_opy_
from bstack_utils.bstack111111ll_opy_ import bstack111l1lll_opy_
class bstack11l11ll1_opy_:
    def __init__(self, args, logger, bstack1lll1lll1_opy_, bstack1lllll11l_opy_):
        self.args = args
        self.logger = logger
        self.bstack1lll1lll1_opy_ = bstack1lll1lll1_opy_
        self.bstack1lllll11l_opy_ = bstack1lllll11l_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1111l1ll_opy_ = []
        self.bstack1llll11ll_opy_ = []
        self.bstack11111111_opy_ = []
        self.bstack111l1ll1_opy_ = self.bstack1111ll11_opy_()
        self.bstack111l1l11_opy_ = -1
    def bstack1llllll1l_opy_(self, bstack111ll1ll_opy_):
        self.parse_args()
        self.bstack11l11lll_opy_()
        self.bstack111ll11l_opy_(bstack111ll1ll_opy_)
        self.bstack1llll1l1l_opy_()
    def bstack1111l11l_opy_(self):
        bstack111111ll_opy_ = bstack111l1lll_opy_.bstack11l11l1l_opy_(self.bstack1lll1lll1_opy_, self.logger)
        if bstack111111ll_opy_ is None:
            self.logger.warn(bstack1l1lll1_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡩࡣࡱࡨࡱ࡫ࡲࠡ࡫ࡶࠤࡳࡵࡴࠡ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡩ࠴ࠠࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥ঒"))
            return
        bstack1llll111l_opy_ = False
        bstack111111ll_opy_.bstack11l1l111_opy_(bstack1l1lll1_opy_ (u"ࠣࡧࡱࡥࡧࡲࡥࡥࠤও"), bstack111111ll_opy_.bstack1llll11l1_opy_())
        start_time = time.time()
        if bstack111111ll_opy_.bstack1llll11l1_opy_():
            test_files = self.bstack1111l111_opy_()
            bstack1llll111l_opy_ = True
            bstack111l111l_opy_ = bstack111111ll_opy_.bstack11l1l11l_opy_(test_files)
            if bstack111l111l_opy_:
                self.bstack1111l1ll_opy_ = [os.path.normpath(item).replace(bstack1l1lll1_opy_ (u"ࠩ࡟ࡠࠬঔ"), bstack1l1lll1_opy_ (u"ࠪ࠳ࠬক")) for item in bstack111l111l_opy_]
                self.__1lllll1ll_opy_()
                bstack111111ll_opy_.bstack111lllll_opy_(bstack1llll111l_opy_)
                self.logger.info(bstack1l1lll1_opy_ (u"࡙ࠦ࡫ࡳࡵࡵࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡵࡴ࡫ࡱ࡫ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤখ").format(self.bstack1111l1ll_opy_))
            else:
                self.logger.info(bstack1l1lll1_opy_ (u"ࠧࡔ࡯ࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡽࡥࡳࡧࠣࡶࡪࡵࡲࡥࡧࡵࡩࡩࠦࡢࡺࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥগ"))
        bstack111111ll_opy_.bstack11l1l111_opy_(bstack1l1lll1_opy_ (u"ࠨࡴࡪ࡯ࡨࡘࡦࡱࡥ࡯ࡖࡲࡅࡵࡶ࡬ࡺࠤঘ"), int((time.time() - start_time) * 1000)) # bstack1llll1111_opy_ to bstack111lll1l_opy_
    def __1lllll1ll_opy_(self):
        bstack1l1lll1_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡋࡵࡲࠡࡧࡤࡧ࡭ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࠢ࡬ࡲࠥࡹࡥ࡭ࡨ࠱ࡷࡵ࡫ࡣࡠࡨ࡬ࡰࡪࡹࠬࠡࡥࡲࡰࡱ࡫ࡣࡵࠢࡤࡰࡱࠦ࡮ࡰࡦࡨ࡭ࡩࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦঙ")
        bstack1llll1ll1_opy_ = []
        try:
            import importlib
            bstack111lll11_opy_ = importlib.import_module(bstack1l1lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࠩচ") + bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡱ࡮ࡸ࡫࡮ࡴ࠮ࡱ࡮ࡸ࡫࡮ࡴࠧছ"))
            get_test_count_and_files = getattr(bstack111lll11_opy_, bstack1l1lll1_opy_ (u"ࠪ࡫ࡪࡺ࡟ࡵࡧࡶࡸࡤࡩ࡯ࡶࡰࡷࡣࡦࡴࡤࡠࡨ࡬ࡰࡪࡹࠧজ"))
            results = get_test_count_and_files(bstack11l111ll_opy_=self.bstack1111l1ll_opy_, bstack1llll1lll_opy_=True)
            bstack1llll1ll1_opy_ = results[bstack1l1lll1_opy_ (u"ࠫࡳࡵࡤࡦ࡫ࡧࡷࠬঝ")]
            os.environ[bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡔࡘࡃࡉࡇࡖࡘࡗࡇࡔࡆࡆࡢࡗࡊࡒࡅࡄࡖࡒࡖࡘ࠭ঞ")] = json.dumps(bstack1llll1ll1_opy_)
        except Exception as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡱࡳࡩ࡫ࠠࡴࡧ࡯ࡩࡨࡺ࡯ࡳࡵ࠽ࠤࢀࢃࠢট").format(str(e)))
            import traceback
            self.logger.error(bstack1l1lll1_opy_ (u"ࠢࡕࡴࡤࡧࡪࡨࡡࡤ࡭࠽ࠤࢀࢃࠢঠ").format(traceback.format_exc()))
            return 0
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack11111lll_opy_():
        import importlib
        if getattr(importlib, bstack1l1lll1_opy_ (u"ࠨࡨ࡬ࡲࡩࡥ࡬ࡰࡣࡧࡩࡷ࠭ড"), False):
            bstack1lllllll1_opy_ = importlib.find_loader(bstack1l1lll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࠫঢ"))
        else:
            bstack1lllllll1_opy_ = importlib.util.find_spec(bstack1l1lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡷࡪࡲࡥ࡯࡫ࡸࡱࠬণ"))
    def bstack111ll111_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack111l1l11_opy_ = -1
        if self.bstack1lllll11l_opy_ and bstack1l1lll1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫত") in self.bstack1lll1lll1_opy_:
            self.bstack111l1l11_opy_ = int(self.bstack1lll1lll1_opy_[bstack1l1lll1_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬথ")])
        try:
            bstack1llllll11_opy_ = [bstack1l1lll1_opy_ (u"࠭࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠨদ"), bstack1l1lll1_opy_ (u"ࠧ࠮࠯ࡳࡰࡺ࡭ࡩ࡯ࡵࠪধ"), bstack1l1lll1_opy_ (u"ࠨ࠯ࡳࠫন")]
            if self.bstack111l1l11_opy_ >= 0:
                bstack1llllll11_opy_.extend([bstack1l1lll1_opy_ (u"ࠩ࠰࠱ࡳࡻ࡭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ঩"), bstack1l1lll1_opy_ (u"ࠪ࠱ࡳ࠭প")])
            for arg in bstack1llllll11_opy_:
                self.bstack111ll111_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack11l11lll_opy_(self):
        bstack1llll11ll_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack1llll11ll_opy_ = bstack1llll11ll_opy_
        return self.bstack1llll11ll_opy_
    def bstack111l11l1_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack11111lll_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack11l11l11_opy_)
    def bstack111ll11l_opy_(self, bstack111ll1ll_opy_):
        bstack1111111l_opy_ = Config.bstack11l11l1l_opy_()
        if bstack111ll1ll_opy_:
            self.bstack1llll11ll_opy_.append(bstack1l1lll1_opy_ (u"ࠫ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨফ"))
            self.bstack1llll11ll_opy_.append(bstack1l1lll1_opy_ (u"࡚ࠬࡲࡶࡧࠪব"))
        if bstack1111111l_opy_.bstack11111ll1_opy_():
            self.bstack1llll11ll_opy_.append(bstack1l1lll1_opy_ (u"࠭࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬভ"))
            self.bstack1llll11ll_opy_.append(bstack1l1lll1_opy_ (u"ࠧࡕࡴࡸࡩࠬম"))
        self.bstack1llll11ll_opy_.append(bstack1l1lll1_opy_ (u"ࠨ࠯ࡳࠫয"))
        self.bstack1llll11ll_opy_.append(bstack1l1lll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡱ࡮ࡸ࡫࡮ࡴࠧর"))
        self.bstack1llll11ll_opy_.append(bstack1l1lll1_opy_ (u"ࠪ࠱࠲ࡪࡲࡪࡸࡨࡶࠬ঱"))
        self.bstack1llll11ll_opy_.append(bstack1l1lll1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫল"))
        if self.bstack111l1l11_opy_ > 1:
            self.bstack1llll11ll_opy_.append(bstack1l1lll1_opy_ (u"ࠬ࠳࡮ࠨ঳"))
            self.bstack1llll11ll_opy_.append(str(self.bstack111l1l11_opy_))
    def bstack1llll1l1l_opy_(self):
        if bstack1111llll_opy_.bstack1lll1l1ll_opy_(self.bstack1lll1lll1_opy_):
             self.bstack1llll11ll_opy_ += [
                bstack11111l11_opy_.get(bstack1l1lll1_opy_ (u"࠭ࡲࡦࡴࡸࡲࠬ঴")), str(bstack1111llll_opy_.bstack1lllll111_opy_(self.bstack1lll1lll1_opy_)),
                bstack11111l11_opy_.get(bstack1l1lll1_opy_ (u"ࠧࡥࡧ࡯ࡥࡾ࠭঵")), str(bstack11111l11_opy_.get(bstack1l1lll1_opy_ (u"ࠨࡴࡨࡶࡺࡴ࠭ࡥࡧ࡯ࡥࡾ࠭শ")))
            ]
    def bstack111l1111_opy_(self):
        bstack11111111_opy_ = []
        for spec in self.bstack1111l1ll_opy_:
            bstack11l11111_opy_ = [spec]
            bstack11l11111_opy_ += self.bstack1llll11ll_opy_
            bstack11111111_opy_.append(bstack11l11111_opy_)
        self.bstack11111111_opy_ = bstack11111111_opy_
        return bstack11111111_opy_
    def bstack1111ll11_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack111l1ll1_opy_ = True
            return True
        except Exception as e:
            self.bstack111l1ll1_opy_ = False
        return self.bstack111l1ll1_opy_
    def bstack1lll1llll_opy_(self):
        bstack1l1lll1_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡋࡪࡺࠠࡵࡪࡨࠤࡨࡵࡵ࡯ࡶࠣࡳ࡫ࠦࡴࡦࡵࡷࡷࠥࡽࡩࡵࡪࡲࡹࡹࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠠࡵࡪࡨࡱࠥࡻࡳࡪࡰࡪࠤࡵࡿࡴࡦࡵࡷࠫࡸࠦ࠭࠮ࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡲࡲࡱࡿࠠࡧ࡮ࡤ࡫࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡱࡸ࠿ࠦࡔࡩࡧࠣࡸࡴࡺࡡ࡭ࠢࡱࡹࡲࡨࡥࡳࠢࡲࡪࠥࡺࡥࡴࡶࡶࠤࡨࡵ࡬࡭ࡧࡦࡸࡪࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧষ")
        try:
            import importlib
            bstack111lll11_opy_ = importlib.import_module(bstack1l1lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࠫস") + bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡳࡰࡺ࡭ࡩ࡯࠰ࡳࡰࡺ࡭ࡩ࡯ࠩহ"))
            get_test_count_and_files = getattr(bstack111lll11_opy_, bstack1l1lll1_opy_ (u"ࠬ࡭ࡥࡵࡡࡷࡩࡸࡺ࡟ࡤࡱࡸࡲࡹࡥࡡ࡯ࡦࡢࡪ࡮ࡲࡥࡴࠩ঺"))
            bstack11111l1l_opy_ = get_test_count_and_files(bstack111l11ll_opy_=self.bstack1llll11ll_opy_, bstack1llll1lll_opy_=True)
            self.logger.info(bstack1l1lll1_opy_ (u"ࠨࡃࡰ࡮࡯ࡩࡨࡺࡥࡥࠢࡾࢁࠥࡺࡥࡴࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡾࢁࠥ࡬ࡩ࡭ࡧࡶࠦ঻").format(bstack11111l1l_opy_[bstack1l1lll1_opy_ (u"ࠧࡤࡱࡸࡲࡹ়࠭")], len(bstack11111l1l_opy_[bstack1l1lll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡦࡪ࡮ࡨࡷࠬঽ")])))
            return bstack11111l1l_opy_[bstack1l1lll1_opy_ (u"ࠩࡦࡳࡺࡴࡴࠨা")]
        except Exception as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡵࡵ࡯ࡶ࠽ࠤࢀࢃࠢি").format(e))
            import traceback
            self.logger.error(bstack1l1lll1_opy_ (u"࡙ࠦࡸࡡࡤࡧࡥࡥࡨࡱ࠺ࠡࡽࢀࠦী").format(traceback.format_exc()))
            return 0
    def bstack1lllll1l1_opy_(self, bstack1llll1l11_opy_, bstack1llllll1l_opy_):
        bstack1llllll1l_opy_[bstack1l1lll1_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬু")] = self.bstack1lll1lll1_opy_
        multiprocessing.set_start_method(bstack1l1lll1_opy_ (u"࠭ࡳࡱࡣࡺࡲࠬূ"))
        bstack111111l1_opy_ = []
        manager = multiprocessing.Manager()
        bstack1lll1ll11_opy_ = manager.list()
        if bstack1l1lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪৃ") in self.bstack1lll1lll1_opy_:
            for index, platform in enumerate(self.bstack1lll1lll1_opy_[bstack1l1lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫৄ")]):
                bstack111111l1_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack1llll1l11_opy_,
                                                            args=(self.bstack1llll11ll_opy_, bstack1llllll1l_opy_, bstack1lll1ll11_opy_)))
            bstack111ll1l1_opy_ = len(self.bstack1lll1lll1_opy_[bstack1l1lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ৅")])
        else:
            bstack111111l1_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack1llll1l11_opy_,
                                                        args=(self.bstack1llll11ll_opy_, bstack1llllll1l_opy_, bstack1lll1ll11_opy_)))
            bstack111ll1l1_opy_ = 1
        i = 0
        for t in bstack111111l1_opy_:
            os.environ[bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪ৆")] = str(i)
            if bstack1l1lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧে") in self.bstack1lll1lll1_opy_:
                os.environ[bstack1l1lll1_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭ৈ")] = json.dumps(self.bstack1lll1lll1_opy_[bstack1l1lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ৉")][i % bstack111ll1l1_opy_])
            i += 1
            t.start()
        for t in bstack111111l1_opy_:
            t.join()
        return list(bstack1lll1ll11_opy_)
    @staticmethod
    def bstack1llllllll_opy_(driver, bstack1111l1l1_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ৊"), None)
        if item and getattr(item, bstack1l1lll1_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤࡩࡡࡴࡧࠪো"), None) and not getattr(item, bstack1l1lll1_opy_ (u"ࠩࡢࡥ࠶࠷ࡹࡠࡵࡷࡳࡵࡥࡤࡰࡰࡨࠫৌ"), False):
            logger.info(
                bstack1l1lll1_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠤ࡭ࡧࡳࠡࡧࡱࡨࡪࡪ࠮ࠡࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡶࡼࡧࡹ࠯ࠤ্"))
            bstack111llll1_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1lll1ll1l_opy_.bstack1111lll1_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack1111l111_opy_(self):
        bstack1l1lll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡹࡵࠠࡣࡧࠣࡩࡽ࡫ࡣࡶࡶࡨࡨࠥࡨࡹࠡࡲࡤࡶࡸ࡯࡮ࡨࠢࡷ࡬ࡪࠦ࡯ࡶࡶࡳࡹࡹࠦ࡯ࡧࠢࡳࡽࡹ࡫ࡳࡵࠢ࠰࠱ࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡵ࡮࡭ࡻ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣৎ")
        try:
            import importlib
            bstack111lll11_opy_ = importlib.import_module(bstack1l1lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤ࠭৏") + bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡵࡲࡵࡨ࡫ࡱ࠲ࡵࡲࡵࡨ࡫ࡱࠫ৐"))
            get_test_count_and_files = getattr(bstack111lll11_opy_, bstack1l1lll1_opy_ (u"ࠧࡨࡧࡷࡣࡹ࡫ࡳࡵࡡࡦࡳࡺࡴࡴࡠࡣࡱࡨࡤ࡬ࡩ࡭ࡧࡶࠫ৑"))
            bstack111l1l1l_opy_ = get_test_count_and_files(bstack111l11ll_opy_=self.bstack1llll11ll_opy_, bstack1llll1lll_opy_=True)
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡅࡲࡰࡱ࡫ࡣࡵࡧࡧࠤࢀࢃࠠࡵࡧࡶࡸࡸࠦࡩ࡯ࠢࡾࢁࠥ࡬ࡩ࡭ࡧࡶࠦ৒").format(bstack111l1l1l_opy_[bstack1l1lll1_opy_ (u"ࠩࡦࡳࡺࡴࡴࠨ৓")], len(bstack111l1l1l_opy_[bstack1l1lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡨ࡬ࡰࡪࡹࠧ৔")])))
            return bstack111l1l1l_opy_[bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡩ࡭ࡱ࡫ࡳࠨ৕")]
        except Exception as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠧ৖").format(e))
            import traceback
            self.logger.error(bstack1l1lll1_opy_ (u"ࠨࡔࡳࡣࡦࡩࡧࡧࡣ࡬࠼ࠣࡿࢂࠨৗ").format(traceback.format_exc()))
            return []