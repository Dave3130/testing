# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1llll1ll_opy_, bstack111l1ll11ll_opy_
from bstack_utils.bstack11l1ll1l11_opy_ import bstack11l11l11l11_opy_
class bstack11lll1l1_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack11111l1l1l1_opy_=None, bstack11111l11l11_opy_=True, bstack1ll1111l11l_opy_=None, bstack1111ll1l1_opy_=None, result=None, duration=None, bstack1l11llll_opy_=None, meta={}):
        self.bstack1l11llll_opy_ = bstack1l11llll_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack11111l11l11_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack11111l1l1l1_opy_ = bstack11111l1l1l1_opy_
        self.bstack1ll1111l11l_opy_ = bstack1ll1111l11l_opy_
        self.bstack1111ll1l1_opy_ = bstack1111ll1l1_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1l11lll1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l1lll1_opy_(self, meta):
        self.meta = meta
    def bstack11ll1l11_opy_(self, hooks):
        self.hooks = hooks
    def bstack11111l1l11l_opy_(self):
        bstack11111l1l111_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack111111l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨờ"): bstack11111l1l111_opy_,
            bstack111111l_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠨỞ"): bstack11111l1l111_opy_,
            bstack111111l_opy_ (u"ࠧࡷࡥࡢࡪ࡮ࡲࡥࡱࡣࡷ࡬ࠬở"): bstack11111l1l111_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack111111l_opy_ (u"ࠣࡗࡱࡩࡽࡶࡥࡤࡶࡨࡨࠥࡧࡲࡨࡷࡰࡩࡳࡺ࠺ࠡࠤỠ") + key)
            setattr(self, key, val)
    def bstack11111l111l1_opy_(self):
        return {
            bstack111111l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧỡ"): self.name,
            bstack111111l_opy_ (u"ࠪࡦࡴࡪࡹࠨỢ"): {
                bstack111111l_opy_ (u"ࠫࡱࡧ࡮ࡨࠩợ"): bstack111111l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬỤ"),
                bstack111111l_opy_ (u"࠭ࡣࡰࡦࡨࠫụ"): self.code
            },
            bstack111111l_opy_ (u"ࠧࡴࡥࡲࡴࡪࡹࠧỦ"): self.scope,
            bstack111111l_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ủ"): self.tags,
            bstack111111l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬỨ"): self.framework,
            bstack111111l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧứ"): self.started_at
        }
    def bstack111111ll1l1_opy_(self):
        return {
         bstack111111l_opy_ (u"ࠫࡲ࡫ࡴࡢࠩỪ"): self.meta
        }
    def bstack11111l111ll_opy_(self):
        return {
            bstack111111l_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡗ࡫ࡲࡶࡰࡓࡥࡷࡧ࡭ࠨừ"): {
                bstack111111l_opy_ (u"࠭ࡲࡦࡴࡸࡲࡤࡴࡡ࡮ࡧࠪỬ"): self.bstack11111l1l1l1_opy_
            }
        }
    def bstack11111l11lll_opy_(self, bstack111111lllll_opy_, details):
        step = next(filter(lambda st: st[bstack111111l_opy_ (u"ࠧࡪࡦࠪử")] == bstack111111lllll_opy_, self.meta[bstack111111l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧỮ")]), None)
        step.update(details)
    def bstack11ll1l1l_opy_(self, bstack111111lllll_opy_):
        step = next(filter(lambda st: st[bstack111111l_opy_ (u"ࠩ࡬ࡨࠬữ")] == bstack111111lllll_opy_, self.meta[bstack111111l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩỰ")]), None)
        step.update({
            bstack111111l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨự"): bstack1llll1ll_opy_()
        })
    def bstack1ll111l1_opy_(self, bstack111111lllll_opy_, result, duration=None):
        bstack1ll1111l11l_opy_ = bstack1llll1ll_opy_()
        if bstack111111lllll_opy_ is not None and self.meta.get(bstack111111l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫỲ")):
            step = next(filter(lambda st: st[bstack111111l_opy_ (u"࠭ࡩࡥࠩỳ")] == bstack111111lllll_opy_, self.meta[bstack111111l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭Ỵ")]), None)
            step.update({
                bstack111111l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ỵ"): bstack1ll1111l11l_opy_,
                bstack111111l_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫỶ"): duration if duration else bstack111l1ll11ll_opy_(step[bstack111111l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧỷ")], bstack1ll1111l11l_opy_),
                bstack111111l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫỸ"): result.result,
                bstack111111l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ỹ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack11111l11ll1_opy_):
        if self.meta.get(bstack111111l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬỺ")):
            self.meta[bstack111111l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ỻ")].append(bstack11111l11ll1_opy_)
        else:
            self.meta[bstack111111l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧỼ")] = [ bstack11111l11ll1_opy_ ]
    def bstack11111l1111l_opy_(self):
        return {
            bstack111111l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧỽ"): self.bstack1l11lll1_opy_(),
            **self.bstack11111l111l1_opy_(),
            **self.bstack11111l1l11l_opy_(),
            **self.bstack111111ll1l1_opy_()
        }
    def bstack111111ll1ll_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack111111l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨỾ"): self.bstack1ll1111l11l_opy_,
            bstack111111l_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬỿ"): self.duration,
            bstack111111l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬἀ"): self.result.result
        }
        if data[bstack111111l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ἁ")] == bstack111111l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧἂ"):
            data[bstack111111l_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧἃ")] = self.result.bstack11111l111l_opy_()
            data[bstack111111l_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪἄ")] = [{bstack111111l_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ἅ"): self.result.bstack111ll111l11_opy_()}]
        return data
    def bstack111111llll1_opy_(self):
        return {
            bstack111111l_opy_ (u"ࠫࡺࡻࡩࡥࠩἆ"): self.bstack1l11lll1_opy_(),
            **self.bstack11111l111l1_opy_(),
            **self.bstack11111l1l11l_opy_(),
            **self.bstack111111ll1ll_opy_(),
            **self.bstack111111ll1l1_opy_()
        }
    def bstack1ll11l11_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack111111l_opy_ (u"࡙ࠬࡴࡢࡴࡷࡩࡩ࠭ἇ") in event:
            return self.bstack11111l1111l_opy_()
        elif bstack111111l_opy_ (u"࠭ࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨἈ") in event:
            return self.bstack111111llll1_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll1111l11l_opy_ = time if time else bstack1llll1ll_opy_()
        self.duration = duration if duration else bstack111l1ll11ll_opy_(self.started_at, self.bstack1ll1111l11l_opy_)
        if result:
            self.result = result
class bstack1ll1llll_opy_(bstack11lll1l1_opy_):
    def __init__(self, hooks=[], bstack1lll11l1_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1lll11l1_opy_ = bstack1lll11l1_opy_
        super().__init__(*args, **kwargs, bstack1111ll1l1_opy_=bstack111111l_opy_ (u"ࠧࡵࡧࡶࡸࠬἉ"))
    @classmethod
    def bstack11111l11l1l_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack111111l_opy_ (u"ࠨ࡫ࡧࠫἊ"): id(step),
                bstack111111l_opy_ (u"ࠩࡷࡩࡽࡺࠧἋ"): step.name,
                bstack111111l_opy_ (u"ࠪ࡯ࡪࡿࡷࡰࡴࡧࠫἌ"): step.keyword,
            })
        return bstack1ll1llll_opy_(
            **kwargs,
            meta={
                bstack111111l_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࠬἍ"): {
                    bstack111111l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪἎ"): feature.name,
                    bstack111111l_opy_ (u"࠭ࡰࡢࡶ࡫ࠫἏ"): feature.filename,
                    bstack111111l_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬἐ"): feature.description
                },
                bstack111111l_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪἑ"): {
                    bstack111111l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧἒ"): scenario.name
                },
                bstack111111l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩἓ"): steps,
                bstack111111l_opy_ (u"ࠫࡪࡾࡡ࡮ࡲ࡯ࡩࡸ࠭ἔ"): bstack11l11l11l11_opy_(test)
            }
        )
    def bstack111111lll11_opy_(self):
        return {
            bstack111111l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫἕ"): self.hooks
        }
    def bstack111111lll1l_opy_(self):
        if self.bstack1lll11l1_opy_:
            return {
                bstack111111l_opy_ (u"࠭ࡩ࡯ࡶࡨ࡫ࡷࡧࡴࡪࡱࡱࡷࠬ἖"): self.bstack1lll11l1_opy_
            }
        return {}
    def bstack111111llll1_opy_(self):
        return {
            **super().bstack111111llll1_opy_(),
            **self.bstack111111lll11_opy_()
        }
    def bstack11111l1111l_opy_(self):
        return {
            **super().bstack11111l1111l_opy_(),
            **self.bstack111111lll1l_opy_()
        }
    def event_key(self):
        return bstack111111l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩ἗")
class bstack1l1l1l11_opy_(bstack11lll1l1_opy_):
    def __init__(self, hook_type, *args,bstack1lll11l1_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l111lll11l_opy_ = None
        self.bstack1lll11l1_opy_ = bstack1lll11l1_opy_
        super().__init__(*args, **kwargs, bstack1111ll1l1_opy_=bstack111111l_opy_ (u"ࠨࡪࡲࡳࡰ࠭Ἐ"))
    def bstack1ll1l1l1_opy_(self):
        return self.hook_type
    def bstack11111l11111_opy_(self):
        return {
            bstack111111l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬἙ"): self.hook_type
        }
    def bstack111111llll1_opy_(self):
        return {
            **super().bstack111111llll1_opy_(),
            **self.bstack11111l11111_opy_()
        }
    def bstack11111l1111l_opy_(self):
        return {
            **super().bstack11111l1111l_opy_(),
            bstack111111l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤ࡯ࡤࠨἚ"): self.bstack1l111lll11l_opy_,
            **self.bstack11111l11111_opy_()
        }
    def event_key(self):
        return bstack111111l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳ࠭Ἓ")
    def bstack11l1llll_opy_(self, bstack1l111lll11l_opy_):
        self.bstack1l111lll11l_opy_ = bstack1l111lll11l_opy_