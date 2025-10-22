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
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1l1lll1_opy_ import bstack11ll1ll11ll_opy_
from bstack_utils.bstack111l1l1l_opy_ import bstack111l11ll_opy_
from bstack_utils.helper import bstack1111l11l1l_opy_
import json
class bstack1lllll1ll_opy_:
    _1ll1l1llll1_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack11111lll1l1_opy_ = bstack11ll1ll11ll_opy_(self.config, logger)
        self.bstack111l1l1l_opy_ = bstack111l11ll_opy_.bstack1111l1ll_opy_(config=self.config)
        self.bstack11111lll11l_opy_ = {}
        self.bstack1lllll1l1_opy_ = False
        self.bstack11111llll11_opy_ = (
            self.__11111llll1l_opy_()
            and self.bstack111l1l1l_opy_ is not None
            and self.bstack111l1l1l_opy_.bstack1llll11ll_opy_()
            and config.get(bstack1lllll1l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧẩ"), None) is not None
            and config.get(bstack1lllll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭Ẫ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack1111l1ll_opy_(cls, config, logger):
        if cls._1ll1l1llll1_opy_ is None and config is not None:
            cls._1ll1l1llll1_opy_ = bstack1lllll1ll_opy_(config, logger)
        return cls._1ll1l1llll1_opy_
    def bstack1llll11ll_opy_(self):
        bstack1lllll1l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡆࡲࠤࡳࡵࡴࠡࡣࡳࡴࡱࡿࠠࡵࡧࡶࡸࠥࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡸࡪࡨࡲ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡔ࠷࠱ࡺࠢ࡬ࡷࠥࡴ࡯ࡵࠢࡨࡲࡦࡨ࡬ࡦࡦࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡑࡵࡨࡪࡸࡩ࡯ࡩࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠠࡪࡵࠣࡒࡴࡴࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠢ࡬ࡷࠥࡔ࡯࡯ࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢẫ")
        return self.bstack11111llll11_opy_ and self.bstack11111llllll_opy_()
    def bstack11111llllll_opy_(self):
        bstack1111l11111l_opy_ = os.getenv(bstack1lllll1l_opy_ (u"ࠬࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࡠࡗࡖࡉࡉ࠭Ậ"), self.config.get(bstack1lllll1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩậ"), None))
        return bstack1111l11111l_opy_ in bstack11l11l1ll1l_opy_
    def __11111llll1l_opy_(self):
        bstack11ll11lll1l_opy_ = False
        for fw in bstack11l1l111lll_opy_:
            if fw in self.config.get(bstack1lllll1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪẮ"), bstack1lllll1l_opy_ (u"ࠨࠩắ")):
                bstack11ll11lll1l_opy_ = True
        return bstack1111l11l1l_opy_(self.config.get(bstack1lllll1l_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭Ằ"), bstack11ll11lll1l_opy_))
    def bstack11111lll1ll_opy_(self):
        return (not self.bstack1llll11ll_opy_() and
                self.bstack111l1l1l_opy_ is not None and self.bstack111l1l1l_opy_.bstack1llll11ll_opy_())
    def bstack1111l111111_opy_(self):
        if not self.bstack11111lll1ll_opy_():
            return
        if self.config.get(bstack1lllll1l_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨằ"), None) is None or self.config.get(bstack1lllll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧẲ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack1lllll1l_opy_ (u"࡚ࠧࡥࡴࡶࠣࡖࡪࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡤࡣࡱࠫࡹࠦࡷࡰࡴ࡮ࠤࡦࡹࠠࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠣࡳࡷࠦࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠤ࡮ࡹࠠ࡯ࡷ࡯ࡰ࠳ࠦࡐ࡭ࡧࡤࡷࡪࠦࡳࡦࡶࠣࡥࠥࡴ࡯࡯࠯ࡱࡹࡱࡲࠠࡷࡣ࡯ࡹࡪ࠴ࠢẳ"))
        if not self.__11111llll1l_opy_():
            self.logger.info(bstack1lllll1l_opy_ (u"ࠨࡔࡦࡵࡷࠤࡗ࡫࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡥࡤࡲࠬࡺࠠࡸࡱࡵ࡯ࠥࡧࡳࠡࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࠡ࡫ࡶࠤࡩ࡯ࡳࡢࡤ࡯ࡩࡩ࠴ࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡦࡰࡤࡦࡱ࡫ࠠࡪࡶࠣࡪࡷࡵ࡭ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠤ࡫࡯࡬ࡦ࠰ࠥẴ"))
    def bstack11111lllll1_opy_(self):
        return self.bstack1lllll1l1_opy_
    def bstack1111l1l1_opy_(self, bstack1111l1111l1_opy_):
        self.bstack1lllll1l1_opy_ = bstack1111l1111l1_opy_
        self.bstack1llllll11_opy_(bstack1lllll1l_opy_ (u"ࠢࡢࡲࡳࡰ࡮࡫ࡤࠣẵ"), bstack1111l1111l1_opy_)
    def bstack1lll11l11_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠣ࡝ࡵࡩࡴࡸࡤࡦࡴࡢࡸࡪࡹࡴࡠࡨ࡬ࡰࡪࡹ࡝ࠡࡐࡲࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡲࡵࡳࡻ࡯ࡤࡦࡦࠣࡪࡴࡸࠠࡰࡴࡧࡩࡷ࡯࡮ࡨ࠰ࠥẶ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack111l1l1l_opy_.bstack111lllll11l_opy_()
            if self.bstack111l1l1l_opy_ is not None:
                orchestration_strategy = self.bstack111l1l1l_opy_.bstack11l1l1ll1_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack1lllll1l_opy_ (u"ࠤࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡶࡸࡷࡧࡴࡦࡩࡼࠤ࡮ࡹࠠࡏࡱࡱࡩ࠳ࠦࡃࡢࡰࡱࡳࡹࠦࡰࡳࡱࡦࡩࡪࡪࠠࡸ࡫ࡷ࡬ࠥࡺࡥࡴࡶࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠲ࠧặ"))
                return None
            self.logger.info(bstack1lllll1l_opy_ (u"ࠥࡖࡪࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡼ࡯ࡴࡩࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡶࡸࡷࡧࡴࡦࡩࡼ࠾ࠥࢁࡽࠣẸ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack1lllll1l_opy_ (u"࡚ࠦࡹࡩ࡯ࡩࠣࡇࡑࡏࠠࡧ࡮ࡲࡻࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠴ࠢẹ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack1lllll1l_opy_ (u"࡛ࠧࡳࡪࡰࡪࠤࡸࡪ࡫ࠡࡨ࡯ࡳࡼࠦࡦࡰࡴࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠮ࠣẺ"))
                self.bstack11111lll1l1_opy_.bstack11ll1ll1ll1_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack11111lll1l1_opy_.bstack11ll1ll111l_opy_()
            if not ordered_test_files:
                return None
            self.bstack1llllll11_opy_(bstack1lllll1l_opy_ (u"ࠨࡵࡱ࡮ࡲࡥࡩ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡆࡳࡺࡴࡴࠣẻ"), len(test_files))
            self.bstack1llllll11_opy_(bstack1lllll1l_opy_ (u"ࠢ࡯ࡱࡧࡩࡎࡴࡤࡦࡺࠥẼ"), int(os.environ.get(bstack1lllll1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡏࡑࡇࡉࡤࡏࡎࡅࡇ࡛ࠦẽ")) or bstack1lllll1l_opy_ (u"ࠤ࠳ࠦẾ")))
            self.bstack1llllll11_opy_(bstack1lllll1l_opy_ (u"ࠥࡸࡴࡺࡡ࡭ࡐࡲࡨࡪࡹࠢế"), int(os.environ.get(bstack1lllll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡒࡔࡊࡅࡠࡅࡒ࡙ࡓ࡚ࠢỀ")) or bstack1lllll1l_opy_ (u"ࠧ࠷ࠢề")))
            self.bstack1llllll11_opy_(bstack1lllll1l_opy_ (u"ࠨࡤࡰࡹࡱࡰࡴࡧࡤࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡈࡵࡵ࡯ࡶࠥỂ"), len(ordered_test_files))
            self.bstack1llllll11_opy_(bstack1lllll1l_opy_ (u"ࠢࡴࡲ࡯࡭ࡹ࡚ࡥࡴࡶࡶࡅࡕࡏࡃࡢ࡮࡯ࡇࡴࡻ࡮ࡵࠤể"), self.bstack11111lll1l1_opy_.bstack11ll1llll1l_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠣ࡝ࡵࡩࡴࡸࡤࡦࡴࡢࡸࡪࡹࡴࡠࡨ࡬ࡰࡪࡹ࡝ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡧࡱࡧࡳࡴࡧࡶ࠾ࠥࢁࡽࠣỄ").format(e))
        return None
    def bstack1llllll11_opy_(self, key, value):
        self.bstack11111lll11l_opy_[key] = value
    def bstack11ll11ll1l_opy_(self):
        return self.bstack11111lll11l_opy_