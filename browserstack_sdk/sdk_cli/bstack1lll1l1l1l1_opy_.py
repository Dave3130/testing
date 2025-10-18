# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llll1l1lll_opy_,
    bstack1llll1l1111_opy_,
    bstack1lll1lllll1_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1l11ll1_opy_, bstack1ll11111ll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import bstack1lllll11l1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_, bstack1lll1l1ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll111_opy_ import bstack1lll11ll11l_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1l1ll_opy_ import bstack1lll1l111l1_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack1lll1l1l11_opy_ import bstack1ll1lll11l_opy_, bstack11ll11lll1_opy_, bstack1lll111lll_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1lll1ll11l1_opy_(bstack1lll1l111l1_opy_):
    bstack1lll1l1lll1_opy_ = bstack11l111_opy_ (u"ࠨࡴࡦࡵࡷࡣࡩࡸࡩࡷࡧࡵࡷࠧᄤ")
    bstack1lll11lll11_opy_ = bstack11l111_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨᄥ")
    bstack1lll11l1lll_opy_ = bstack11l111_opy_ (u"ࠣࡰࡲࡲࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥᄦ")
    bstack1lll1ll1l1l_opy_ = bstack11l111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤᄧ")
    bstack1lll1l11l1l_opy_ = bstack11l111_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡡࡵࡩ࡫ࡹࠢᄨ")
    bstack1llll111l1l_opy_ = bstack11l111_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡦࡶࡪࡧࡴࡦࡦࠥᄩ")
    bstack1llll1111ll_opy_ = bstack11l111_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡲࡦࡳࡥࠣᄪ")
    bstack1llll111111_opy_ = bstack11l111_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡸࡺࡡࡵࡷࡶࠦᄫ")
    def __init__(self):
        super().__init__(bstack1llll11l111_opy_=self.bstack1lll1l1lll1_opy_, frameworks=[bstack1lllll11l1l_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllllll11l_opy_((bstack1lll1ll1lll_opy_.BEFORE_EACH, bstack1lll11lll1l_opy_.POST), self.bstack1lll1l1ll11_opy_)
        if bstack1ll11111ll_opy_():
            TestFramework.bstack1lllllll11l_opy_((bstack1lll1ll1lll_opy_.TEST, bstack1lll11lll1l_opy_.POST), self.bstack1llll111lll_opy_)
        else:
            TestFramework.bstack1lllllll11l_opy_((bstack1lll1ll1lll_opy_.TEST, bstack1lll11lll1l_opy_.PRE), self.bstack1llll111lll_opy_)
        TestFramework.bstack1lllllll11l_opy_((bstack1lll1ll1lll_opy_.TEST, bstack1lll11lll1l_opy_.POST), self.bstack1lll1llll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1l1ll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll11ll1ll_opy_ = self.bstack1lll1lll1ll_opy_(instance.context)
        if not bstack1lll11ll1ll_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡵࡧࡧࡦ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧᄬ") + str(bstack1lllll1ll11_opy_) + bstack11l111_opy_ (u"ࠣࠤᄭ"))
            return
        f.bstack1llllllll1l_opy_(instance, bstack1lll1ll11l1_opy_.bstack1lll11lll11_opy_, bstack1lll11ll1ll_opy_)
    def bstack1lll1lll1ll_opy_(self, context: bstack1lll1lllll1_opy_, bstack1lll1l11lll_opy_= True):
        if bstack1lll1l11lll_opy_:
            bstack1lll11ll1ll_opy_ = self.bstack1lll11ll1l1_opy_(context, reverse=True)
        else:
            bstack1lll11ll1ll_opy_ = self.bstack1lll1ll11ll_opy_(context, reverse=True)
        return [f for f in bstack1lll11ll1ll_opy_ if f[1].state != bstack1lllll1lll1_opy_.QUIT]
    def bstack1llll111lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1ll11_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        if not bstack1lll1l11ll1_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄮ") + str(kwargs) + bstack11l111_opy_ (u"ࠥࠦᄯ"))
            return
        bstack1lll11ll1ll_opy_ = f.get_state(instance, bstack1lll1ll11l1_opy_.bstack1lll11lll11_opy_, [])
        if not bstack1lll11ll1ll_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄰ") + str(kwargs) + bstack11l111_opy_ (u"ࠧࠨᄱ"))
            return
        if len(bstack1lll11ll1ll_opy_) > 1:
            self.logger.debug(
                bstack11l1ll1l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡰࡢࡩࡨࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣᄲ"))
        bstack1lll1l1l111_opy_, bstack1lll1llllll_opy_ = bstack1lll11ll1ll_opy_[0]
        page = bstack1lll1l1l111_opy_()
        if not page:
            self.logger.debug(bstack11l111_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄳ") + str(kwargs) + bstack11l111_opy_ (u"ࠣࠤᄴ"))
            return
        bstack11l111l1l_opy_ = getattr(args[0], bstack11l111_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᄵ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11l111_opy_ (u"ࠥࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠣᄶ")).get(bstack11l111_opy_ (u"ࠦࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨᄷ")):
            try:
                page.evaluate(bstack11l111_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᄸ"),
                            bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪᄹ") + json.dumps(
                                bstack11l111l1l_opy_) + bstack11l111_opy_ (u"ࠢࡾࡿࠥᄺ"))
            except Exception as e:
                self.logger.debug(bstack11l111_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࠨᄻ"), e)
    def bstack1lll1llll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1ll11_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        if not bstack1lll1l11ll1_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄼ") + str(kwargs) + bstack11l111_opy_ (u"ࠥࠦᄽ"))
            return
        bstack1lll11ll1ll_opy_ = f.get_state(instance, bstack1lll1ll11l1_opy_.bstack1lll11lll11_opy_, [])
        if not bstack1lll11ll1ll_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄾ") + str(kwargs) + bstack11l111_opy_ (u"ࠧࠨᄿ"))
            return
        if len(bstack1lll11ll1ll_opy_) > 1:
            self.logger.debug(
                bstack11l1ll1l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡰࡢࡩࡨࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣᅀ"))
        bstack1lll1l1l111_opy_, bstack1lll1llllll_opy_ = bstack1lll11ll1ll_opy_[0]
        page = bstack1lll1l1l111_opy_()
        if not page:
            self.logger.debug(bstack11l111_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᅁ") + str(kwargs) + bstack11l111_opy_ (u"ࠣࠤᅂ"))
            return
        status = f.get_state(instance, TestFramework.bstack1llll1111l1_opy_, None)
        if not status:
            self.logger.debug(bstack11l111_opy_ (u"ࠤࡱࡳࠥࡹࡴࡢࡶࡸࡷࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࠬࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧᅃ") + str(bstack1lllll1ll11_opy_) + bstack11l111_opy_ (u"ࠥࠦᅄ"))
            return
        bstack1llll111l11_opy_ = {bstack11l111_opy_ (u"ࠦࡸࡺࡡࡵࡷࡶࠦᅅ"): status.lower()}
        bstack1lll1l1llll_opy_ = f.get_state(instance, TestFramework.bstack1lll1ll1ll1_opy_, None)
        if status.lower() == bstack11l111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᅆ") and bstack1lll1l1llll_opy_ is not None:
            bstack1llll111l11_opy_[bstack11l111_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ᅇ")] = bstack1lll1l1llll_opy_[0][bstack11l111_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪᅈ")][0] if isinstance(bstack1lll1l1llll_opy_, list) else str(bstack1lll1l1llll_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11l111_opy_ (u"ࠣࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸࠨᅉ")).get(bstack11l111_opy_ (u"ࠤࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨᅊ")):
            try:
                page.evaluate(
                        bstack11l111_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦᅋ"),
                        bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࠩᅌ")
                        + json.dumps(bstack1llll111l11_opy_)
                        + bstack11l111_opy_ (u"ࠧࢃࠢᅍ")
                    )
            except Exception as e:
                self.logger.debug(bstack11l111_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣࡿࢂࠨᅎ"), e)
    def bstack1lll1ll111l_opy_(
        self,
        instance: bstack1lll1l1ll1l_opy_,
        f: TestFramework,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1ll11_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        if not bstack1lll1l11ll1_opy_:
            self.logger.debug(
                bstack11l1ll1l_opy_ (u"ࠢ࡮ࡣࡵ࡯ࡤࡵ࠱࠲ࡻࡢࡷࡾࡴࡣ࠻ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣᅏ"))
            return
        bstack1lll11ll1ll_opy_ = f.get_state(instance, bstack1lll1ll11l1_opy_.bstack1lll11lll11_opy_, [])
        if not bstack1lll11ll1ll_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᅐ") + str(kwargs) + bstack11l111_opy_ (u"ࠤࠥᅑ"))
            return
        if len(bstack1lll11ll1ll_opy_) > 1:
            self.logger.debug(
                bstack11l1ll1l_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࢁ࡬ࡦࡰࠫࡴࡦ࡭ࡥࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࡰࡽࡡࡳࡩࡶࢁࠧᅒ"))
        bstack1lll1l1l111_opy_, bstack1lll1llllll_opy_ = bstack1lll11ll1ll_opy_[0]
        page = bstack1lll1l1l111_opy_()
        if not page:
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡲࡧࡲ࡬ࡡࡲ࠵࠶ࡿ࡟ࡴࡻࡱࡧ࠿ࠦ࡮ࡰࠢࡳࡥ࡬࡫ࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᅓ") + str(kwargs) + bstack11l111_opy_ (u"ࠧࠨᅔ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack11l111_opy_ (u"ࠨࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࡙ࡹ࡯ࡥ࠽ࠦᅕ") + str(timestamp)
        try:
            page.evaluate(
                bstack11l111_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣᅖ"),
                bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭ᅗ").format(
                    json.dumps(
                        {
                            bstack11l111_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࠤᅘ"): bstack11l111_opy_ (u"ࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧᅙ"),
                            bstack11l111_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᅚ"): {
                                bstack11l111_opy_ (u"ࠧࡺࡹࡱࡧࠥᅛ"): bstack11l111_opy_ (u"ࠨࡁ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠥᅜ"),
                                bstack11l111_opy_ (u"ࠢࡥࡣࡷࡥࠧᅝ"): data,
                                bstack11l111_opy_ (u"ࠣ࡮ࡨࡺࡪࡲࠢᅞ"): bstack11l111_opy_ (u"ࠤࡧࡩࡧࡻࡧࠣᅟ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack11l111_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦ࡯࠲࠳ࡼࠤࡦࡴ࡮ࡰࡶࡤࡸ࡮ࡵ࡮ࠡ࡯ࡤࡶࡰ࡯࡮ࡨࠢࡾࢁࠧᅠ"), e)
    def bstack1lll1llll11_opy_(
        self,
        instance: bstack1lll1l1ll1l_opy_,
        f: TestFramework,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l1ll11_opy_(f, instance, bstack1lllll1ll11_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1lll1ll11l1_opy_.bstack1llll111l1l_opy_, False):
            return
        self.bstack1llll1lll11_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llllllll11_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1l11l11_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll11ll111_opy_)
        req.test_framework_state = bstack1lllll1ll11_opy_[0].name
        req.test_hook_state = bstack1lllll1ll11_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll1lll1l1_opy_)
        for bstack1lll1l11111_opy_ in bstack1lll11ll11l_opy_.bstack1lll11llll1_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack11l111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠥᅡ")
                if bstack1lll1l11ll1_opy_
                else bstack11l111_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࡥࡧࡳ࡫ࡧࠦᅢ")
            )
            session.ref = bstack1lll1l11111_opy_.ref()
            session.hub_url = bstack1lll11ll11l_opy_.get_state(bstack1lll1l11111_opy_, bstack1lll11ll11l_opy_.bstack1llll111ll1_opy_, bstack11l111_opy_ (u"ࠨࠢᅣ"))
            session.framework_name = bstack1lll1l11111_opy_.framework_name
            session.framework_version = bstack1lll1l11111_opy_.framework_version
            session.framework_session_id = bstack1lll11ll11l_opy_.get_state(bstack1lll1l11111_opy_, bstack1lll11ll11l_opy_.bstack1lll1ll1l11_opy_, bstack11l111_opy_ (u"ࠢࠣᅤ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1l1111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11ll1ll_opy_ = f.get_state(instance, bstack1lll1ll11l1_opy_.bstack1lll11lll11_opy_, [])
        if not bstack1lll11ll1ll_opy_:
            self.logger.debug(bstack11l111_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᅥ") + str(kwargs) + bstack11l111_opy_ (u"ࠤࠥᅦ"))
            return
        if len(bstack1lll11ll1ll_opy_) > 1:
            self.logger.debug(bstack11l111_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࢁ࡬ࡦࡰࠫࡴࡦ࡭ࡥࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᅧ") + str(kwargs) + bstack11l111_opy_ (u"ࠦࠧᅨ"))
        bstack1lll1l1l111_opy_, bstack1lll1llllll_opy_ = bstack1lll11ll1ll_opy_[0]
        page = bstack1lll1l1l111_opy_()
        if not page:
            self.logger.debug(bstack11l111_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᅩ") + str(kwargs) + bstack11l111_opy_ (u"ࠨࠢᅪ"))
            return
        return page
    def bstack1lll11lllll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1lll1l1l11l_opy_ = {}
        for bstack1lll1l11111_opy_ in bstack1lll11ll11l_opy_.bstack1lll11llll1_opy_.values():
            caps = bstack1lll11ll11l_opy_.get_state(bstack1lll1l11111_opy_, bstack1lll11ll11l_opy_.bstack1lll1ll1111_opy_, bstack11l111_opy_ (u"ࠢࠣᅫ"))
        bstack1lll1l1l11l_opy_[bstack11l111_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࠨᅬ")] = caps.get(bstack11l111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࠥᅭ"), bstack11l111_opy_ (u"ࠥࠦᅮ"))
        bstack1lll1l1l11l_opy_[bstack11l111_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥᅯ")] = caps.get(bstack11l111_opy_ (u"ࠧࡵࡳࠣᅰ"), bstack11l111_opy_ (u"ࠨࠢᅱ"))
        bstack1lll1l1l11l_opy_[bstack11l111_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤᅲ")] = caps.get(bstack11l111_opy_ (u"ࠣࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧᅳ"), bstack11l111_opy_ (u"ࠤࠥᅴ"))
        bstack1lll1l1l11l_opy_[bstack11l111_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠦᅵ")] = caps.get(bstack11l111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳࠨᅶ"), bstack11l111_opy_ (u"ࠧࠨᅷ"))
        return bstack1lll1l1l11l_opy_
    def bstack1lll1lll11l_opy_(self, page: object, bstack1llll11111l_opy_, args={}):
        try:
            bstack1lll1l111ll_opy_ = bstack11l111_opy_ (u"ࠨࠢࠣࠪࡩࡹࡳࡩࡴࡪࡱࡱࠤ࠭࠴࠮࠯ࡤࡶࡸࡦࡩ࡫ࡔࡦ࡮ࡅࡷ࡭ࡳࠪࠢࡾࡿࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡳࡧࡷࡹࡷࡴࠠ࡯ࡧࡺࠤࡕࡸ࡯࡮࡫ࡶࡩ࠭࠮ࡲࡦࡵࡲࡰࡻ࡫ࠬࠡࡴࡨ࡮ࡪࡩࡴࠪࠢࡀࡂࠥࢁࡻࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡣࡵࡷࡥࡨࡱࡓࡥ࡭ࡄࡶ࡬ࡹ࠮ࡱࡷࡶ࡬࠭ࡸࡥࡴࡱ࡯ࡺࡪ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡼࡨࡱࡣࡧࡵࡤࡺࡿࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࡽࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࢀ࠭࠭ࢁࡡࡳࡩࡢ࡮ࡸࡵ࡮ࡾࠫࠥࠦࠧᅸ")
            bstack1llll11111l_opy_ = bstack1llll11111l_opy_.replace(bstack11l111_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᅹ"), bstack11l111_opy_ (u"ࠣࡤࡶࡸࡦࡩ࡫ࡔࡦ࡮ࡅࡷ࡭ࡳࠣᅺ"))
            script = bstack1lll1l111ll_opy_.format(fn_body=bstack1llll11111l_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠤࡤ࠵࠶ࡿ࡟ࡴࡥࡵ࡭ࡵࡺ࡟ࡦࡺࡨࡧࡺࡺࡥ࠻ࠢࡈࡶࡷࡵࡲࠡࡧࡻࡩࡨࡻࡴࡪࡰࡪࠤࡹ࡮ࡥࠡࡣ࠴࠵ࡾࠦࡳࡤࡴ࡬ࡴࡹ࠲ࠠࠣᅻ") + str(e) + bstack11l111_opy_ (u"ࠥࠦᅼ"))