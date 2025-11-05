# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1lll111_opy_ import bstack11ll1ll1l1l_opy_
from bstack_utils.bstack1lll1ll11_opy_ import bstack111l11ll_opy_
from bstack_utils.helper import bstack1l1111l1ll_opy_
import json
class bstack1llll111l_opy_:
    _1ll1l1lll11_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack11111ll11l1_opy_ = bstack11ll1ll1l1l_opy_(self.config, logger)
        self.bstack1lll1ll11_opy_ = bstack111l11ll_opy_.bstack1111llll_opy_(config=self.config)
        self.bstack11111ll1l11_opy_ = {}
        self.bstack1llll11ll_opy_ = False
        self.bstack11111ll1111_opy_ = (
            self.__11111ll1lll_opy_()
            and self.bstack1lll1ll11_opy_ is not None
            and self.bstack1lll1ll11_opy_.bstack1lll1ll1l_opy_()
            and config.get(bstack11111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩỜ"), None) is not None
            and config.get(bstack11111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨờ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack1111llll_opy_(cls, config, logger):
        if cls._1ll1l1lll11_opy_ is None and config is not None:
            cls._1ll1l1lll11_opy_ = bstack1llll111l_opy_(config, logger)
        return cls._1ll1l1lll11_opy_
    def bstack1lll1ll1l_opy_(self):
        bstack11111_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡈࡴࠦ࡮ࡰࡶࠣࡥࡵࡶ࡬ࡺࠢࡷࡩࡸࡺࠠࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡺ࡬ࡪࡴ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡏ࠲࠳ࡼࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡪࡴࡡࡣ࡮ࡨࡨࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡓࡷࡪࡥࡳ࡫ࡱ࡫ࠥ࡯ࡳࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠢ࡬ࡷࠥࡔ࡯࡯ࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠤ࡮ࡹࠠࡏࡱࡱࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤỞ")
        return self.bstack11111ll1111_opy_ and self.bstack11111ll1ll1_opy_()
    def bstack11111ll1ll1_opy_(self):
        bstack11111ll1l1l_opy_ = os.getenv(bstack11111_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨở"), self.config.get(bstack11111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫỠ"), None))
        return bstack11111ll1l1l_opy_ in bstack11l11llllll_opy_
    def __11111ll1lll_opy_(self):
        bstack11ll11l11l1_opy_ = False
        for fw in bstack11l11ll1lll_opy_:
            if fw in self.config.get(bstack11111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬỡ"), bstack11111_opy_ (u"ࠪࠫỢ")):
                bstack11ll11l11l1_opy_ = True
        return bstack1l1111l1ll_opy_(self.config.get(bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨợ"), bstack11ll11l11l1_opy_))
    def bstack11111lll11l_opy_(self):
        return (not self.bstack1lll1ll1l_opy_() and
                self.bstack1lll1ll11_opy_ is not None and self.bstack1lll1ll11_opy_.bstack1lll1ll1l_opy_())
    def bstack11111ll111l_opy_(self):
        if not self.bstack11111lll11l_opy_():
            return
        if self.config.get(bstack11111_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪỤ"), None) is None or self.config.get(bstack11111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩụ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack11111_opy_ (u"ࠢࡕࡧࡶࡸࠥࡘࡥࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡦࡥࡳ࠭ࡴࠡࡹࡲࡶࡰࠦࡡࡴࠢࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠥࡵࡲࠡࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࠦࡩࡴࠢࡱࡹࡱࡲ࠮ࠡࡒ࡯ࡩࡦࡹࡥࠡࡵࡨࡸࠥࡧࠠ࡯ࡱࡱ࠱ࡳࡻ࡬࡭ࠢࡹࡥࡱࡻࡥ࠯ࠤỦ"))
        if not self.__11111ll1lll_opy_():
            self.logger.info(bstack11111_opy_ (u"ࠣࡖࡨࡷࡹࠦࡒࡦࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡧࡦࡴࠧࡵࠢࡺࡳࡷࡱࠠࡢࡵࠣࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡤࡪࡵࡤࡦࡱ࡫ࡤ࠯ࠢࡓࡰࡪࡧࡳࡦࠢࡨࡲࡦࡨ࡬ࡦࠢ࡬ࡸࠥ࡬ࡲࡰ࡯ࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱࠦࡦࡪ࡮ࡨ࠲ࠧủ"))
    def bstack11111lll111_opy_(self):
        return self.bstack1llll11ll_opy_
    def bstack1lllll111_opy_(self, bstack11111ll11ll_opy_):
        self.bstack1llll11ll_opy_ = bstack11111ll11ll_opy_
        self.bstack111ll11l_opy_(bstack11111_opy_ (u"ࠤࡤࡴࡵࡲࡩࡦࡦࠥỨ"), bstack11111ll11ll_opy_)
    def bstack1lll1111l_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack11111_opy_ (u"ࠥ࡟ࡷ࡫࡯ࡳࡦࡨࡶࡤࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴ࡟ࠣࡒࡴࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡴࡷࡵࡶࡪࡦࡨࡨࠥ࡬࡯ࡳࠢࡲࡶࡩ࡫ࡲࡪࡰࡪ࠲ࠧứ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack1lll1ll11_opy_.bstack111lll11111_opy_()
            if self.bstack1lll1ll11_opy_ is not None:
                orchestration_strategy = self.bstack1lll1ll11_opy_.bstack11llll1lll_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack11111_opy_ (u"ࠦࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡸࡺࡲࡢࡶࡨ࡫ࡾࠦࡩࡴࠢࡑࡳࡳ࡫࠮ࠡࡅࡤࡲࡳࡵࡴࠡࡲࡵࡳࡨ࡫ࡥࡥࠢࡺ࡭ࡹ࡮ࠠࡵࡧࡶࡸࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠴ࠢỪ"))
                return None
            self.logger.info(bstack11111_opy_ (u"ࠧࡘࡥࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡷࡪࡶ࡫ࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡸࡺࡲࡢࡶࡨ࡫ࡾࡀࠠࡼࡿࠥừ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack11111_opy_ (u"ࠨࡕࡴ࡫ࡱ࡫ࠥࡉࡌࡊࠢࡩࡰࡴࡽࠠࡧࡱࡵࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠯ࠤỬ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack11111_opy_ (u"ࠢࡖࡵ࡬ࡲ࡬ࠦࡳࡥ࡭ࠣࡪࡱࡵࡷࠡࡨࡲࡶࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥử"))
                self.bstack11111ll11l1_opy_.bstack11ll1l1ll11_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack11111ll11l1_opy_.bstack11ll1l1lll1_opy_()
            if not ordered_test_files:
                return None
            self.bstack111ll11l_opy_(bstack11111_opy_ (u"ࠣࡷࡳࡰࡴࡧࡤࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡈࡵࡵ࡯ࡶࠥỮ"), len(test_files))
            self.bstack111ll11l_opy_(bstack11111_opy_ (u"ࠤࡱࡳࡩ࡫ࡉ࡯ࡦࡨࡼࠧữ"), int(os.environ.get(bstack11111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡑࡓࡉࡋ࡟ࡊࡐࡇࡉ࡝ࠨỰ")) or bstack11111_opy_ (u"ࠦ࠵ࠨự")))
            self.bstack111ll11l_opy_(bstack11111_opy_ (u"ࠧࡺ࡯ࡵࡣ࡯ࡒࡴࡪࡥࡴࠤỲ"), int(os.environ.get(bstack11111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡔࡏࡅࡇࡢࡇࡔ࡛ࡎࡕࠤỳ")) or bstack11111_opy_ (u"ࠢ࠲ࠤỴ")))
            self.bstack111ll11l_opy_(bstack11111_opy_ (u"ࠣࡦࡲࡻࡳࡲ࡯ࡢࡦࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹࡃࡰࡷࡱࡸࠧỵ"), len(ordered_test_files))
            self.bstack111ll11l_opy_(bstack11111_opy_ (u"ࠤࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡇࡐࡊࡅࡤࡰࡱࡉ࡯ࡶࡰࡷࠦỶ"), self.bstack11111ll11l1_opy_.bstack11ll1ll1ll1_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack11111_opy_ (u"ࠥ࡟ࡷ࡫࡯ࡳࡦࡨࡶࡤࡺࡥࡴࡶࡢࡪ࡮ࡲࡥࡴ࡟ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩ࡬ࡢࡵࡶࡩࡸࡀࠠࡼࡿࠥỷ").format(e))
        return None
    def bstack111ll11l_opy_(self, key, value):
        self.bstack11111ll1l11_opy_[key] = value
    def bstack11l1lll1l1_opy_(self):
        return self.bstack11111ll1l11_opy_